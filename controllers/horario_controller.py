from flask import jsonify, send_from_directory

UPLOAD_FOLDER = 'uploads'

class HorarioController:
    @staticmethod
    def horario_file(filehorario):
        try:
            return send_from_directory(UPLOAD_FOLDER, filehorario, as_attachment=True)
        except FileNotFoundError:
            return jsonify({"error": "Arquivo não encontrado"}), 404