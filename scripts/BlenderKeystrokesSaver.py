import bpy
import datetime
import os
import bmesh
from bpy.app.handlers import persistent

LOG_DIR = r"I:\atomic_project\scripts\BlenderKeystrokesSaver_logs"
START_TIME = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# Pamięć podręczna
last_op_entry = ""
last_vert_entry = ""
last_obj_entry = ""
initial_vert_coords = {} 
initial_obj_dims = {} # Przechowuje Loc/Rot/Scale obiektów

def get_atomic_path():
    filename = f"{START_TIME}-BlenderKeystrokesSaver.log"
    return os.path.join(LOG_DIR, filename)

def write_to_log(message, entry_type="ANY"):
    global last_op_entry, last_vert_entry, last_obj_entry
    
    if entry_type == "OP":
        if message == last_op_entry: return
        last_op_entry = message
    elif entry_type == "VERT":
        if message == last_vert_entry: return
        last_vert_entry = message
    elif entry_type == "OBJ":
        if message == last_obj_entry: return
        last_obj_entry = message

    path = get_atomic_path()
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
    except:
        pass

@persistent
def track_everything(scene):
    global initial_vert_coords, initial_obj_dims
    obj = bpy.context.active_object
    if not obj: return

    # 1. ŚLEDZENIE TRANSFORMACJI ORIGINU (OBJECT MODE & EDIT MODE)
    # Pobieramy aktualne dane transformacji
    curr_loc = obj.location.copy()
    curr_rot = [rad * (180/3.14159) for rad in obj.rotation_euler] # Na stopnie dla ludzkiego oka
    curr_scale = obj.scale.copy()
    
    obj_name = obj.name
    
    # Sprawdzamy czy to ruch (translate/rotate/resize)
    current_op = ""
    if hasattr(bpy.context, "window_manager") and bpy.context.window_manager.operators:
        current_op = bpy.context.window_manager.operators[-1].bl_idname
    
    is_transform = any(x in current_op for x in ("translate", "rotate", "resize"))

    if is_transform:
        # Jeśli nie mamy zapisanego stanu początkowego obiektu
        if obj_name not in initial_obj_dims:
            initial_obj_dims[obj_name] = {
                'loc': curr_loc.copy(),
                'rot': list(curr_rot),
                'scale': curr_scale.copy()
            }
        
        pre = initial_obj_dims[obj_name]
        
        # Obliczamy różnice (czy nastąpiła zmiana względem PRE)
        loc_diff = (curr_loc - pre['loc']).length > 0.001
        rot_diff = sum([abs(curr_rot[i] - pre['rot'][i]) for i in range(3)]) > 0.1
        scale_diff = (curr_scale - pre['scale']).length > 0.001

        if loc_diff or rot_diff or scale_diff:
            obj_msg = f"OBJECT_ORIGIN | {obj_name} | TRANSFORMING...\n"
            if loc_diff: obj_msg += f"  -> LOC: PRE{pre['loc'].to_tuple(2)} -> POST{curr_loc.to_tuple(2)}\n"
            if rot_diff: obj_msg += f"  -> ROT: PRE({pre['rot'][0]:.1f}, {pre['rot'][1]:.1f}, {pre['rot'][2]:.1f}) -> POST({curr_rot[0]:.1f}, {curr_rot[1]:.1f}, {curr_rot[2]:.1f})\n"
            if scale_diff: obj_msg += f"  -> SCALE: PRE{pre['scale'].to_tuple(2)} -> POST{curr_scale.to_tuple(2)}"
            write_to_log(obj_msg.strip(), entry_type="OBJ")
    else:
        initial_obj_dims.clear() # Czyścimy gdy nie ma aktywnej transformacji

    # 2. ŚLEDZENIE WIERZCHOŁKÓW (EDIT MODE)
    if obj.mode == 'EDIT' and obj.type == 'MESH':
        bm = bmesh.from_edit_mesh(obj.data)
        matrix = obj.matrix_world
        selected_verts = [v for v in bm.verts if v.select]
        
        if selected_verts:
            vert_indices = [v.index for v in selected_verts]
            pos_details = ""
            
            if is_transform:
                for v in selected_verts:
                    curr_v_pos = matrix @ v.co
                    if v.index not in initial_vert_coords:
                        initial_vert_coords[v.index] = curr_v_pos.copy()
                    
                    start_v_pos = initial_vert_coords[v.index]
                    if (curr_v_pos - start_v_pos).length > 0.001:
                        pos_details += f"\n  -> V{v.index} PRE{start_v_pos.to_tuple(2)} -> POST{curr_v_pos.to_tuple(2)}"
            else:
                initial_vert_coords.clear()

            write_to_log(f"VERTS | {obj_name} | {vert_indices}" + pos_details, entry_type="VERT")

    # 3. ŚLEDZENIE KOMEND
    if hasattr(bpy.context, "window_manager") and bpy.context.window_manager.operators:
        op = bpy.context.window_manager.operators[-1]
        write_to_log(f"KOMENDA: {op.name} ({op.bl_idname})", entry_type="OP")

def register():
    bpy.app.handlers.depsgraph_update_post.clear()
    bpy.app.handlers.depsgraph_update_post.append(track_everything)
    write_to_log(f"=== SESJA ATOMIC START: {START_TIME} ===")

if __name__ == "__main__":
    register()