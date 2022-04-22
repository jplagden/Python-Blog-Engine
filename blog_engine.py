import os
import os.path
    

# create entry .html file
# put the title into such file
# update the index.html




#selects the most current file in the 'articles' directory
def select_current_article ():

    blogFiles= os.listdir(os.getcwd() + '/articles')
    return blogFiles[len(blogFiles) - 1]

#gets the title (first line) of the most current file    
def get_title ():
    
    with open('/home/mebious/Files/blog engine/articles/' + select_current_article()) as f:

        lines = f.readlines()
    title = lines[0]
    title = title.replace('\n', '')
    return title

#gets the rest of the text of the most current file
def get_text():
    with open('/home/mebious/Files/blog engine/articles/' + select_current_article()) as f:
        lines = f.readlines()
        lines[0] = ' '
        ret_str = ''
        for line in lines:
            if line.strip('\n') != " " or "\n":
                ret_str += line
        return ret_str

#write the title and text to the html file
def write_to_file():
    title = get_title()
    with open(title + '.html', 'w') as f:
        f.write(get_template())

    with open(title + '.html', 'r+') as f:
        content = f.readlines()
        i = 0

        for line in content:

            if "<h1>" in line:
                content[i] = line.replace("title", title)
                print (content[i])
            i += 1

#get the template html file 
def get_template():
    with open('/home/mebious/Files/blog engine/template.html') as f:
        template = f.read()

    return template  


print (get_title())
print (get_text())
write_to_file()

