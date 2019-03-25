import math


def vector_2d(x1, y1, x2, y2):

    # AB = [(Bx-Ax),(By-Ay)]

    return vector_3d(x1, y1, 0, x2, y2, 0)


def vector_3d(x1, y1, z1, x2, y2, z2):

    # AB = [(Bx-Ax),(By-Ay),(Bz-Az)]

    return [x2 - x1, y2 - y1, z2 - z1]


def vector_addition(vector_a, vector_b):

    # AB + CD = [(ABx+CDx),(ABy+CDy),(ABz+CDz)]

    return [vector_a[0] + vector_b[0], vector_a[1] + vector_b[1], vector_a[2] + vector_b[2]]


def vector_magnitude(vector):

    # |AB| = Square_root_of( (ABx^2) + (ABy^2) )

    return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))


def point_along_vector_given_x(vector, starting_point, x):

    # y=ax+b
    # ax = hight/length(x-x1)
    # b = y1

    m = vector[1]/vector[0]
    ax = (m*x)-(m*starting_point[0])
    y = starting_point[1]

    return [x, ax+y]


def vector_scalar(vector_a, vector_b):

    # AB * CD = ABx*CDx+ABy*CDy+ABz*CDz

    return vector_a[0]*vector_b[0]+vector_a[1]*vector_b[1]+vector_a[2]*vector_b[2]


def angle_between_two_vectors(vector_a, vecotr_b):

    # ∠ABC = BA * BC / |BA|*|BC|*COS(θ) = 0

    BA_scal_BC = vector_scalar(vector_a, vecotr_b)
    BA_mag = vector_magnitude(vector_a)
    BC_mag = vector_magnitude(vecotr_b)

    return math.degrees(math.acos(BA_scal_BC/(BA_mag*BC_mag)))
