def extract_line_number(patch_text):
    for i, line in enumerate(patch_text.splitlines()):
        if line.startswith("+") and not line.startswith("+++"):
            return i
    return 1
