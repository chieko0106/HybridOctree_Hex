# -*- coding: utf-8 -*-
"""
Convert OBJ file to RAW format.
This script reads an OBJ file and converts it to a RAW format.
Usage:
    python obj2raw.py input.obj output.raw

Where:
    input.obj is the path to the input OBJ file.
    output.raw is the path to the output RAW file.
"""
def obj_to_raw(obj_file, raw_file):
    vertices = []
    elements = []

    # 读取OBJ文件并解析顶点和面
    with open(obj_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if parts[0] == 'v':
                # 处理顶点
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                vertices.append((x, y, z))
            elif parts[0] == 'f':
                # 处理面，分解为三角形
                face_vertex_indices = []
                for part in parts[1:]:
                    vertex_part = part.split('/')[0]
                    vertex_index = int(vertex_part) - 1 # 转换为0-based索引
                    face_vertex_indices.append(vertex_index)
                # 分解面为多个三角形
                num_vertices = len(face_vertex_indices)
                for i in range(1, num_vertices - 1):
                    elem = [
                        face_vertex_indices[0],
                        face_vertex_indices[i],
                        face_vertex_indices[i + 1]
                    ]
                    elements.append(elem)

    # 写入RAW文件
    with open(raw_file, 'w') as f:
        f.write(f"{len(vertices)} {len(elements)}\n")
        for v in vertices:
            f.write(f"{v[0]} {v[1]} {v[2]}\n")
        for elem in elements:
            f.write(f"{elem[0]} {elem[1]} {elem[2]}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python obj2raw.py input.obj output.raw")
        sys.exit(1)
    obj_file = sys.argv[1]
    raw_file = sys.argv[2]
    obj_to_raw(obj_file, raw_file)