from flask import jsonify, request

import os

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class UploadController:
    @staticmethod
    def allowed_file(filehorario):
        return '.' in filehorario and filehorario.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    @staticmethod
    def upload_file():
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        
        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Nome do arquivo vazio"}), 400
        
        if file and UploadController.allowed_file(file.filehorario):
            filehorario = secure_filename(file.file)
            file.save(os.path.join(UPLOAD_FOLDER, filehorario))
            return jsonify({"message": "Arquivo salvo com sucesso!", "filename": filehorario}), 200
        else:
            return jsonify({"error": "Arquivo não permitido"}), 400