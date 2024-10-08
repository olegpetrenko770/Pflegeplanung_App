from flask import Flask, render_template, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from backend.main.models import User, Pflegeplan, Pflegebericht
from backend import db
from backend import create_app

# Insert the code block at line 112, column 53

db.session.commit()

# Insert the code block at line 112, column 53

app = create_app()

if __name__ == '__main__':
    app.run()

pflege_app = Flask(__name__)
pflege_app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Setze den geheimen Schlüssel für JWT
jwt = JWTManager(pflege_app)

@pflege_app.route('/')
def home():
    return render_template('index.html')

@pflege_app.route('/example')
def example():
    return jsonify({'message': 'Example response'})

@pflege_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Ungültige Eingabe!'}), 400

        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message': 'Benutzername bereits vergeben!'}), 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Benutzer erfolgreich registriert!'}), 201
    return render_template('register.html')

@pflege_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity={'username': user.username})
            return jsonify({'message': 'Anmeldung erfolgreich!', 'access_token': access_token}), 200
        return jsonify({'message': 'Anmeldung fehlgeschlagen!'}), 401
    return render_template('login.html')

@pflege_app.route('/pflegeplan', methods=['GET', 'POST'])
@jwt_required()
def create_pflegeplan():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(username=get_jwt_identity()['username']).first()
        if user:
            new_pflegeplan = Pflegeplan(
                patientenname=data['patientenname'],
                informationen=data.get('informationen'),
                probleme_ressourcen=data.get('probleme_ressourcen'),
                pflegeziele=data.get('pflegeziele'),
                pflegemassnahmen=data.get('pflegemassnahmen'),
                durchfuehrung=data.get('durchfuehrung'),
                beurteilung=data.get('beurteilung'),
                user_id=user.id
            )
            db.session.add(new_pflegeplan)
            db.session.commit()
            return jsonify({'message': 'Pflegeplan erfolgreich erstellt!'}), 201
        return jsonify({'message': 'Benutzer nicht gefunden!'}), 404
    return render_template('pflegeplan.html')

@pflege_app.route('/pflegebericht', methods=['GET', 'POST'])
@jwt_required()
def create_pflegebericht():
    if request.method == 'POST':
        data = request.get_json()
        pflegeplan = Pflegeplan.query.get(data['pflegeplan_id'])
        if pflegeplan:
            new_bericht = Pflegebericht(
                datum=data['datum'],
                inhalt=data['inhalt'],
                pflegeplan_id=pflegeplan.id
            )
            db.session.add(new_bericht)
            db.session.commit()
            return jsonify({'message': 'Pflegebericht erfolgreich erstellt!'}), 201
        return jsonify({'message': 'Pflegeplan nicht gefunden!'}), 404
    return render_template('pflegebericht.html')

@pflege_app.route('/pflegeplaene', methods=['GET'])
@jwt_required()
def get_pflegeplaene():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    if user:
        pflegeplaene = Pflegeplan.query.filter_by(user_id=user.id).all()
        return jsonify([pflegeplan.to_dict() for pflegeplan in pflegeplaene]), 200
    return jsonify({'message': 'Benutzer nicht gefunden!'}), 404

@pflege_app.route('/pflegeberichte/<int:pflegeplan_id>', methods=['GET'])
@jwt_required()
def get_pflegeberichte(pflegeplan_id):
    pflegeberichte = Pflegebericht.query.filter_by(pflegeplan_id=pflegeplan_id).all()
    return jsonify([bericht.to_dict() for bericht in pflegeberichte]), 200

@pflege_app.route('/pflegebericht/<int:id>', methods=['DELETE'])
@jwt_required()

def delete_pflegebericht(id):
    pflegebericht = Pflegebericht.query.get(id)
    if pflegebericht:
        db.session.delete(pflegebericht)
        db.session.commit()
        return jsonify({'message': 'Pflegebericht erfolgreich gelöscht!'}), 200
    return jsonify({'message': 'Pflegebericht nicht gefunden!'}), 404

@pflege_app.route('/pflegeplan/<int:id>', methods=['PUT'])
@jwt_required()
def update_pflegeplan(id):
    data = request.get_json()
    pflegeplan = Pflegeplan.query.get(id)
    if pflegeplan:
        pflegeplan.patientenname = data.get('patientenname', pflegeplan.patientenname)
        pflegeplan.informationen = data.get('informationen', pflegeplan.informationen)
        pflegeplan.probleme_ressourcen = data.get('probleme_ressourcen', pflegeplan.probleme_ressourcen)
        pflegeplan.pflegeziele = data.get('pflegeziele', pflegeplan.pflegeziele)
        pflegeplan.pflegemassnahmen = data.get('pflegemassnahmen', pflegeplan.pflegemassnahmen)
        pflegeplan.durchfuehrung = data.get('durchfuehrung', pflegeplan.durchfuehrung)
        pflegeplan.beurteilung = data.get('beurteilung', pflegeplan.beurteilung)
        db.session.commit()
        return jsonify({'message': 'Pflegeplan erfolgreich aktualisiert!'}), 200
    return jsonify({'message': 'Pflegeplan nicht gefunden!'}), 404

@pflege_app.route('/pflegebericht/<int:id>', methods=['PUT'])
@jwt_required()
def update_pflegebericht(id):
    data = request.get_json()
    pflegebericht = Pflegebericht.query.get(id)
    if pflegebericht:
        pflegebericht.datum = data.get('datum', pflegebericht.datum)
        pflegebericht.inhalt = data.get('inhalt', pflegebericht.inhalt)
        db.session.commit()
        return jsonify({'message': 'Pflegebericht erfolgreich aktualisiert!'}), 200
    return jsonify({'message': 'Pflegebericht nicht gefunden!'}), 404

# Allgemeine Fehlerbehandlung
@pflege_app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Ressource nicht gefunden!'}), 404

@pflege_app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Interner Serverfehler!'}), 500

if __name__ == '__main__':
    pflege_app.run(debug=True, host='0.0.0.0', port=5000)
