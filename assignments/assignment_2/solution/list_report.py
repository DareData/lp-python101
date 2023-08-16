original_list = ["peixinhos", "pastel", "canja", "bacalhau", "francesinha", "caldo verde",
                 "sardinhas", "cozido", "alheira", "pastel", "bacalhau"]

print(f"Original list: {original_list}")

print(f'The original list has {len(original_list)} elements')

modified_list = original_list.copy()

modified_list[0] = "peixinhos da horta"

modified_list = list(set(modified_list))

modified_list.reverse()

print(f"Modified list: {modified_list}")