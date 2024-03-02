def gen_report(*pages):
    return (f"page {i + 1}: {page}" for i, page in enumerate(pages))


report = gen_report("Стр 1", "Стр 2")
print(report)