from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import RecetaForm, ChangePasswordForm
from app.models import db, Receta, User

# Blueprint principal que maneja el dashboard, gestión de cursos y cambio de contraseña
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        # Verifica que la contraseña actual sea correcta
        if not current_user.check_password(form.old_password.data):
            flash('Current password is incorrect.')  # 🔁 Traducido
            return render_template('cambiar_password.html', form=form)

        # Actualiza la contraseña y guarda
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('✅ Password updated successfully.')  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    return render_template('cambiar_password.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role.name == 'Usuario': # Change this for your project
        recetas = Receta.query.all()
    else:
        recetas = Receta.query.filter_by(usuario_id=current_user.id).all()

    return render_template('dashboard.html', recetas=recetas)

@main.route('/recetas', methods=['GET', 'POST'])
@login_required
def recetas():
    form = RecetaForm()
    if form.validate_on_submit():
        receta = Receta(
            nombre=form.nombre.data,
            ingredientes=form.ingredientes.data,
            instrucciones=form.instrucciones.data,
            tiempo_preparacion=form.tiempo_preparacion.data,
            porciones=form.porciones.data,
            imagen_url=form.imagen_url.data,
            categoria=form.categoria.data,
            usuario_id=current_user.id
        )
        db.session.add(receta)
        db.session.commit()
        flash("Recipe created successfully.")  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    return render_template('receta_form.html', form=form)

@main.route('/recetas/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_receta(id):
    receta = Receta.query.get_or_404(id)

    # Validación de permisos
    if current_user.role.name not in ['Admin', 'Chef'] or (
        receta.usuario_id != current_user.id and current_user.role.name != 'Admin'):
        flash('You do not have permission to edit this recipe.')  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    form = RecetaForm(obj=receta)

    if form.validate_on_submit():
        receta.nombre = form.nombre.data
        receta.ingredientes = form.ingredientes.data
        receta.instrucciones = form.instrucciones.data
        receta.tiempo_preparacion = form.tiempo_preparacion.data
        receta.porciones = form.porciones.data
        receta.imagen_url = form.imagen_url.data
        receta.categoria = form.categoria.data
        db.session.commit()
        flash("Recipe updated successfully.")  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    return render_template('receta_form.html', form=form, editar=True)

@main.route('/recetas/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_receta(id):
    receta = Receta.query.get_or_404(id)

    if current_user.role.name not in ['Admin', 'Chef'] or (
        receta.usuario_id != current_user.id and current_user.role.name != 'Admin'):
        flash('You do not have permission to delete this course.')  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    db.session.delete(receta)
    db.session.commit()
    flash("Recipe deleted successfully.")  # 🔁 Traducido
    return redirect(url_for('main.dashboard'))

@main.route('/usuarios')
@login_required
def listar_usuarios():
    if current_user.role.name != 'Admin':
        flash("You do not have permission to view this page.")
        return redirect(url_for('main.dashboard'))

    # Obtener instancias completas de usuarios con sus roles (no usar .add_columns)
    usuarios = User.query.join(User.role).all()

    return render_template('usuarios.html', usuarios=usuarios)
