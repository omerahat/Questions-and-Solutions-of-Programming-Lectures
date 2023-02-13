import os

current_dir_path = os.getcwd()
reading_file_name = "example_input.txt"
reading_file_path = os.path.join(current_dir_path, reading_file_name)

# Reading a file safe from close() function.
with open(reading_file_path, "r") as f:
	
	data = f.readlines()

print(data)
# data variable now contains my entire file content in string format.

student_list = [["Hayriye", "Çelik", "b2210765059"], ["Cemal", "Yıldız", "b2210055081"]]

writing_file_name = "example_output.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)

# Write to a file safe from close() function.
with open(writing_file_path,"w") as f:
    f.write("Column1\tColumn2\tColumn3\n")
    
    for student in student_list:
        f.write("\t".join(student)+"\n")
    
    #OR
    f.write("\n\nOR\n")
    f.write("Column1\tColumnName2\tColumn3\n")
    for student in student_list:
        f.write(student[0]+"\t"+student[1]+"\t\t"+student[2]+"\n")

    #OR
    f.write("\n\nOR\n")
    output_string = """Column1\tColumnName2\tColumn3
Hayriye\tÇelik\t\tb2210765059
Cem\tYıldız\t\tb2210055081"""
    
    f.writelines(output_string)
    
    #OR
    f.write("\n\nOR\n")
    output_string = "Column1\tColumnName2\tColumn3\nHayriye\tÇelik\t\tb2210765059\n\Cem\tYıldız\t\tb2210055081\n"
    
    f.writelines(output_string)
