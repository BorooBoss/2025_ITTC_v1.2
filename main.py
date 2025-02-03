import dearpygui.dearpygui as dpg
import json
import os

SETTINGS_FILE = "settings.json"

def save_settings(image_path):
    """Uloží cestu k obrázku do JSON súboru."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"image": image_path}, f)

def load_settings():
    """Načíta cestu k poslednému obrázku zo súboru."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)
            return data.get("image", None)
    return None

def clear_settings():
    """Vymaže obsah súboru settings.json pri ukončení aplikácie."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as f:
            json.dump({"image": ""}, f)  # Vyprázdnime súbor

def file_selected_callback(sender, app_data):
    """Funkcia, ktorá sa zavolá po výbere súboru v dialógu."""
    file_path = app_data["file_path_name"]
    
    if file_path and os.path.exists(file_path):
        try:
            width, height, channels, data = dpg.load_image(file_path)
            print(f"Načítaný obrázok: {file_path}, Rozmery: {width}x{height}, Kanály: {channels}")

            dpg.delete_item("image_container", children_only=True)  # Vymaže starý obrázok
            with dpg.texture_registry(show=False):
                dpg.add_static_texture(width, height, data, tag="loaded_texture")

            dpg.add_image("loaded_texture", parent="image_container")  # Pridá obrázok do GUI
            save_settings(file_path)  # Uloží cestu k obrázku
        except Exception as e:
            print(f"Chyba pri načítaní obrázka: {e}")

# Vytvorenie GUI
dpg.create_context()
dpg.create_viewport(title="Image Loader", resizable=False, decorated=False)

# Nastavenie fixnej veľkosti a pozície okna (800x800 v ľavom hornom rohu)
dpg.set_viewport_width(600)
dpg.set_viewport_height(600)
#dpg.set_viewport_pos((5, 5))


# Registrácia textúr
with dpg.texture_registry(show=False):
    pass

with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected_callback, tag="file_dialog", width=700, height=400):
    dpg.add_file_extension("Image Files (*.png *.jpg *.jpeg *.bmp){.png,.jpg,.jpeg,.bmp}")

with dpg.window(label="ICTT v1.0", width=800, height=800, no_move = True):
    dpg.add_spacer(width=5)  # Adjust the width to shift buttons to the right
    dpg.add_same_line()
    dpg.add_button(label="Load image", width=180, height=50, callback=lambda: dpg.show_item("file_dialog")) 
    dpg.add_same_line()
    dpg.add_button(label="Exit", width=180, height=50, callback=lambda: dpg.stop_dearpygui())
    dpg.add_same_line()
    dpg.add_button(label="Minimize", width=180, height=50, callback=lambda: dpg.minimize_viewport())

    dpg.add_separator()
    dpg.add_text("Loaded image:")
    with dpg.group(tag="image_container"):
        pass  # Sem sa pridá obrázok
    

# Načítanie posledného obrázka pri štarte
last_image = load_settings()
if last_image and os.path.exists(last_image):
    try:
        width, height, channels, data = dpg.load_image(last_image)
        dpg.add_static_texture(width, height, data, tag="loaded_texture")
        dpg.add_image("loaded_texture", parent="image_container")
    except Exception as e:
        print(f"Chyba pri načítaní posledného obrázka: {e}")

dpg.setup_dearpygui()
dpg.show_viewport()

# Hlavná slučka
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

# Po zatvorení okna vymažeme nastavenia
clear_settings()

# Ukončenie aplikácie
dpg.destroy_context()