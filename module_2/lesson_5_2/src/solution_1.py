company_name = input()
long_half_name = int(len(company_name)) // 2
slice_company_name = company_name[0:long_half_name]
slice_company_name_2 = company_name[long_half_name:]
print(f"{slice_company_name_2}{slice_company_name}")