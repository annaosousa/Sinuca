import math
import numpy as np
import config


def point_distance(p1,p2):
    dist_diff = p1-p2
    return np.hypot(*dist_diff)

def distance_less_equal(p1,p2,dist):
    dist_diff = p1,p2
    return (dist_diff[0] ** 2 + dist_diff[1] ** 2) <= dist ** 2

def ball_collision_check(ball1, ball2):
    return distance_less_equal(balls1.pos, ball2.pos, 2*config.ball_radius) and \
        np.count_nonzero(np.concatenate((ball1.velocity, ball2.velocity))) > 0 and\
        np.dot(ball2.pos - ball1.pos, ball1.velocity - ball2.velocity) > 0

def collide_balls(ball1, ball2):
    point_diff = ball2.pos - ball1.pos
    dist = point_distance(ball1.pos, ball2.pos)
    collision = point_diff/dist
    ball1_dot = np.dot(ball1.velocity, collision)
    ball2_dot = np.dot(ball2.velocity, collision)
    ball.velocity += (ball2_dot - ball1_dot) * collision * 0.5*(1+config.ball_coeff_of_restituion)


def rotation_matriz(axis, theta):
    axis = np.asarray(axis)
    axis = axis/math.sqrt(np.dot(axis,axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis * math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d 
    return np.array([[aa + bb - cc - dd,2 * (bc+ad), 2 * (bd-ac)],
                    [2 * (bc - ad),aa + cc - bb - dd,2 * (cd + ab)],
                    [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

def line_ball_collision_check(line, ball):
    if distance_less_equal(line.middle, ball.pos, line.length/2 + config.ball_radius):
        displacement_to_ball = ball.pos - line.line[0]
        displacement_to_second_point = line.line[1] - line.line[0]
        normalised_point_diff_vector = displacement_to_second_point / \
            np.hypot(*(displacement_to_second_point))
        projected_distance = np.dot(normalised_point_diff_vector, displacement_to_ball)
        closet_line_point = proprojected_distance * normalised_point_diff_vector
        perpendicular_vector = np.array(
            [-normalised_point_diff_vector[1], normalised_point_diff_vector[0]]
            )
        return -config.ball_radius/3 <= projected_distance <= \
            np.hypot(*(displacement_to_second_point)) + config.ball_radius /3 and \
            np.hypot(*(closest_line_point - ball.pos + line.line[0])) <= \
            config.ball_radius and np.dot(perpendicular_vector, ball.velocity) <= 0

def collide_line_ball(line, ball):
        displacement_to_second_point = line.line[1] - line.line[0]
        normalised_point_diff_vector = displacement_to_second_point / \
            np.hypot(*(displacement_to_second_point))
        perpendicular_vector = np.array(
            [-normalised_point_diff_vector[1], normalised_point_diff_vector[0]])
        ball.velocity -= 2 * np.dot(perpendicular_vector, ball.velocity) * \
            perpendicular_vector * 0.5 *(1+config.table_coeff_of_restitution)