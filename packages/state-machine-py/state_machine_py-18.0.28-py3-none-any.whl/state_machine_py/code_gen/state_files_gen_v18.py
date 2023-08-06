from state_machine_py.code_gen.file_io_v11n80 import FileIoV11n80
from state_machine_py.code_gen.state_file_gen_v18 import StateFileGen
from state_machine_py.conf_obj.transition_v16n3 import TransitionV16n3


def gen_state_files_v18(
    const,
    transition,
    import_module_path,
    output_dir_path,
):

    # エッジの一覧
    edge_list = transition.create_edge_list_v16n2()
    # デバッグ表示
    for edge in edge_list:
        print(f"[gen_state_files_v18] edge={edge}")

    # フォルダーが無ければ作る
    FileIoV11n80.makedirs(output_dir_path)

    # ノードの一覧
    node_path_set = TransitionV16n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        StateFileGen().generate_state_file_v18(
            const=const,
            transition=transition,
            node_path=node_path,
            import_module_path=import_module_path,
            output_dir_path=output_dir_path,
        )
