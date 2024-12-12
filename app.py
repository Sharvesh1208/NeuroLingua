import os
import folium
from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize Firebase
# try:
#     firebase_admin.get_app()
# except ValueError:
#     cred = credentials.Certificate({
#         "type": "service_account",
#         "project_id": "snippetscript-37175",
#         "private_key_id": "your_private_key_id",
#         "private_key": "your_private_key",
#         "client_email": "your_client_email",
#         "client_id": "your_client_id",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "your_cert_url"
#     })
#     firebase_admin.initialize_app(cred)

# Initialize Firestore
# db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     phone = request.form['loginPhone']
#     password = request.form['loginPassword']

#     # Query Firestore to find user
#     users_ref = db.collection('users')
#     query = users_ref.where('phone', '==', phone).where('password', '==', password)
    
#     try:
#         users = query.stream()
#         user_list = list(users)
        
#         if len(user_list) > 0:
#             # User found, start session
#             session['user_phone'] = phone
#             return redirect(url_for('user_dashboard'))
#         else:
#             return "Invalid credentials", 401
    
#     except Exception as e:
#         return str(e), 500

# @app.route('/dashboard')
# def user_dashboard():
#     if 'user_phone' not in session:
#         return redirect(url_for('index'))
    
#     # Fetch user details from Firestore
#     user_ref = db.collection('users').document(session['user_phone'])
#     user = user_ref.get()
    
#     if user.exists:
#         user_data = user.to_dict()
#         return render_template('user-dashboard.html', user=user_data)
#     else:
        # return "User not found", 404

@app.route('/admin')
def admin():
    # Create a map centered on Delhi
    delhi_coordinates = [28.6139, 77.2090]
    folium_map = folium.Map(location=delhi_coordinates, zoom_start=12)

    # Add predefined markers in Delhi
    markers = [
        {"name": "India Gate", "coordinates": [28.6129, 77.2295]},
        {"name": "Red Fort", "coordinates": [28.6562, 77.2410]},
        {"name": "Qutub Minar", "coordinates": [28.5245, 77.1855]},
    ]

    # Add markers to the map
    for marker in markers:
        folium.Marker(
            location=marker["coordinates"],
            popup=marker["name"],
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(folium_map)

    # Use a valid Folium tile layer
    folium.TileLayer('OpenStreetMap').add_to(folium_map)

    # Add Layer Control for toggling between tile layers
    folium.LayerControl().add_to(folium_map)

    # Generate the map HTML
    map_html = folium_map._repr_html_()

    # Render the template with the map
    return render_template('admin.html', map=map_html)

@app.route('/logout')
def logout():
    session.pop('user_phone', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)