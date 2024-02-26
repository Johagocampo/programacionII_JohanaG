from actividad import estudiante

e = estudiante("Johana","apellido","identificacion","correo","celular")
print(e.obtenernombre())

e = estudiante("Johana","Gonzalez","identificacion","correo","celular")
print(e.obtenerapellido())

e = estudiante("Johana","Gonzalez","1048439162","correo","celular")
print(e.obteneridentificacion())

e = estudiante("Johana","Gonzalez","1048439162","johagocampo31@outlook.com","celular")
print(e.obtenercorreo())

e = estudiante("Johana","Gonzalez","1048439162","johagocampo31@outlook.com","3022594936")
print(e.obtenercelular())