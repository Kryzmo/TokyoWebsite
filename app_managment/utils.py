import os
from app_managment.config import Config
from app_managment.error_handler import Error

def icons() -> dict:
    icons_qs = {}
    from xml.dom import minidom
    directory = os.fsencode(rf"{Config.STATIC_URL}icons"[1:])
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".svg"):
            doc = minidom.parse(f"{Config.STATIC_URL}icons/{filename}"[1:])
            path_strings = [path.getAttribute('d') for path
                            in doc.getElementsByTagName('path')]
            doc.unlink()
            try:
                icons_qs.update({f"{filename}".replace(".svg", "").replace('-', '_'): f"{path_strings.pop()}"})
            except Exception as e: Error(e)
    return icons_qs