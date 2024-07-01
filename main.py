import View.gui_app as v
import controller.sql_server_starter as sql_starter
import model as m

print("\n\ndo you have the my sql database?\n y/Y-yes else-no")
letter = input()

if (letter.upper()=='Y'):
    sql_starter.database_initialization()
print(f"your letter is : {letter.upper()}")
app = v.GUIApp()
app.mainloop()