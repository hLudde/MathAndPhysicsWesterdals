import MathAPI


# Oppgavesett 1 a)


OA = MathAPI.vector_2d(0, 0, -1, 2)
OB = MathAPI.vector_2d(0, 0, 0, -1)
OC = MathAPI.vector_2d(0, 0, 2, 1)

print("Oppgavesett 1 a)")
print("A = " + OA.__str__())
print("B = " + OB.__str__())
print("C = " + OC.__str__())
print("")

# Oppgavesett 1 b)


AB = MathAPI.vector_2d(OA[0], OA[1], OB[0], OB[1])
BC = MathAPI.vector_2d(OB[0], OB[1], OC[0], OC[1])
CA = MathAPI.vector_2d(OC[0], OC[1], OA[0], OA[1])
AC = MathAPI.vector_2d(OA[0], OA[1], OC[0], OC[1])

print("Oppgavesett 1 b)")
print("AB = " + AB.__str__())
print("BC = " + BC.__str__())
print("CA = " + CA.__str__())
print("AC = " + AC.__str__())
print("")

# Oppgavesett 1 c)

OX = MathAPI.vector_addition(OA, BC)

print("Oppgavesett 1 c)")
print("OX = " + OX.__str__())
print("X = (" + OX[0].__str__() + ", " + OX[1].__str__() + ")")
print("")

# Oppgavesett 1 d)

OY = MathAPI.point_along_vector_given_x(AC, OA, 1)

print("Oppgavesett 1 d)")
print("OY = " + OY.__str__())
print("")

# Oppgavesett 1 e)

AB_mag = MathAPI.vector_magnitude(AB)
BC_mag = MathAPI.vector_magnitude(BC)
CA_mag = MathAPI.vector_magnitude(CA)

print("Oppgavesett 1 e)")
print("|AB| = " + AB_mag.__str__())
print("|BC| = " + BC_mag.__str__())
print("|CA| = " + CA_mag.__str__())
print("")

# Oppgavesett 1 f)

BA = MathAPI.vector_2d(OB[0], OB[1], OA[0], OA[1])
CB = MathAPI.vector_2d(OC[0], OC[1], OB[0], OB[1])

AB_scalar_AC = MathAPI.vector_scalar(AB, AC)
BC_scalar_BA = MathAPI.vector_scalar(BC, BA)
CA_scalar_CB = MathAPI.vector_scalar(CA, CB)

print("Oppgavesett 1 f)")
print("AB*AC = " + AB_scalar_AC.__str__())
print("BC*BA = " + BC_scalar_BA.__str__())
print("CA*CB = " + CA_scalar_CB.__str__())
print("")

# Oppgavesett 1 g)

CAB_angle = MathAPI.angle_between_two_vectors(AC, AB)
ABC_angle = MathAPI.angle_between_two_vectors(BA, BC)
BCA_angle = MathAPI.angle_between_two_vectors(CA, CB)

print("Oppgavesett 1 g)")
print("∠CAB = " + CAB_angle.__str__())
print("∠ABC = " + ABC_angle.__str__())
print("∠BCA = " + BCA_angle.__str__())
print("")

# Oppgavesett 1 h)

# OD = [x, 3]
# ∠CAD = 60deg
# find x
#
# AC = [3, -1]
# AD = [x-3, 4]
#
# AC * AD = |AC| * |AD| * cos(60)
#
# (ACx*ADx) + (ACy*ADy) = sqrt( ACx^2 + ACy^2 ) * sqrt( ADx^2 + ADy^2) * cos(60)
#
# ( 3 * ( x - 3 ) ) + ( -1 * 4 ) = sqrt( 3^2 + (-1)^2 ) * sqrt( (x-3)^2 + 4^2 ) * cos(60)
#
# 3x - 9 - 4 = sqrt( 9 + 1 ) * sqrt( x^2 - 6x + 9 + 16 ) * cos(60)
#
# 3x - 13 = sqrt( 10 ) * sqrt( x^2 - 6x + 25 ) * cos(60)
#
# 3x / ( sqrt( x^2 - 6x + 25 ) ) = sqrt( 10 ) * cos(60) + 13


# fuck this shit


print("Oppgavesett 1 h)")
print("Fuck this...")
print("")
