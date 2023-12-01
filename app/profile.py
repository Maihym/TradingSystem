#profile.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import User
from db import db

profile_bp = Blueprint('profile', __name__)

# User Profile Page
@profile_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# Edit User Profile
@profile_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        user = current_user
        user.balance = float(request.form.get('balance'))
        user.risk_tolerance = float(request.form.get('risk_tolerance'))

        db.session.commit()
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('profile.profile'))

    return render_template('edit_profile.html', user=current_user)
