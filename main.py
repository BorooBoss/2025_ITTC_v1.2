import dearpygui.dearpygui as dpg
import json
import os
import extract

SETTINGS_FILE = "settings.json"

def save_settings(image_path):
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"image": image_path}, f)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)
            return data.get("image", None)
    return None

def clear_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as f:
            json.dump({"image": ""}, f)  


def resize_image(width, height):
    window_width = dpg.get_viewport_width() - 15  
    window_height = dpg.get_viewport_height() - 100  

    aspect_ratio = width / height

    if width > window_width or height > window_height:
        if width / window_width > height / window_height:
            new_width = window_width
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = window_height
            new_width = int(new_height * aspect_ratio)
    else:
        new_width, new_height = width, height

    return new_width, new_height

def file_selected_callback(sender, app_data): #draw picture and print extracted text after image pick 
    file_path = app_data["file_path_name"]
    
    if file_path and os.path.exists(file_path):
        try:
            width, height, channels, data = dpg.load_image(file_path)
            new_width, new_height = resize_image(width, height)

            if dpg.does_item_exist("image_display"): #delete old image if exists so no conflicts 
                dpg.delete_item("image_display")

            if dpg.does_item_exist("loaded_texture"): #delete old texture bounded to image if exists
                dpg.delete_item("loaded_texture")


            with dpg.texture_registry(): #new static texture to registry, new image draw tied with the texture
                dpg.add_static_texture(width, height, data, tag="loaded_texture")
            dpg.add_image("loaded_texture", parent="image_container", tag="image_display", width=new_width, height=new_height)

            save_settings(file_path) #new output print
            extracted_text = extract.image_to_string(file_path)
            dpg.set_value(output_text_tag, extracted_text)

        except Exception as e:
            print(f"Error while loading image: {e}")

dpg.create_context()
dpg.create_viewport(title="Image Loader", resizable=False, decorated=False)
dpg.set_viewport_width(580)
dpg.set_viewport_height(590)


empty_data = [255, 255, 255, 0]
with dpg.texture_registry(show=False): #setting default texture for images
    dpg.add_static_texture(1, 1, empty_data, tag="loaded_texture")

with dpg.file_dialog(directory_selector=False, show=False, callback=file_selected_callback, tag="file_dialog", width=700, height=400): #explorer settings
    dpg.add_file_extension("Image Files (*.png *.jpg *.jpeg *.bmp){.png,.jpg,.jpeg,.bmp}")

with dpg.window(label="ICTT v1.1", width=600, height=590): #main window settings
    dpg.add_button(label="Load image", width=190, height=50, callback=lambda: dpg.show_item("file_dialog")) 
    dpg.add_same_line()
    dpg.add_button(label="Exit", width=180, height=50, callback=lambda: dpg.stop_dearpygui())
    dpg.add_same_line()
    dpg.add_button(label="Minimize", width=180, height=50, callback=lambda: dpg.minimize_viewport())

    dpg.add_separator()
    dpg.add_text("Loaded image:")
    with dpg.group(tag="image_container"):
        pass  # Sem sa pridá obrázok

    dpg.add_separator()
    dpg.add_text("Extracted Text:")

    #output_text_tag = dpg.add_text("", tag="output_text", wrap=590)
    output_text_tag = dpg.add_input_text(multiline=True, width= dpg.get_viewport_width() - 15)

#extracted_text = extract.image_to_string()
#dpg.set_value(output_text_tag, extracted_text)



dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running(): #main loop
    
    dpg.render_dearpygui_frame()

clear_settings()
dpg.destroy_context()
