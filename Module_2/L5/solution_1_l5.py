company_name = input()
len_name = len(company_name) // 2
rename_company = company_name[len_name:] + company_name[:len_name] 
print(rename_company)