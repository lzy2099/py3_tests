#! /usr/bin/python3
import cgi
import yate
import athletemodel
athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Time of Athletes"))
print(yate.header('Athlete:'+athlete_name+', DOB: '+athletes[athlete_name].dob+'.'))
print(yate.para('The top times for this athlete are:'))
print(yate.para("Top 3 times:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html","Another Athlete":"generate_list.py"}))
