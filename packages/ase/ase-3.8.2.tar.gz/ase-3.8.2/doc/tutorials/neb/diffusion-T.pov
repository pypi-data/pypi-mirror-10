#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {orthographic
  right -13.07*x up 13.10*y
  direction 1.00*z
  location <0,0,50.00> look_at <0,0,0>}
light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}

#declare simple = finish {phong 0.7}
#declare pale = finish {ambient .5 diffuse .85 roughness .001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.10 roughness 0.04 }
#declare vmd = finish {ambient .0 diffuse .65 phong 0.1 phong_size 40. specular 0.500 }
#declare jmol = finish {ambient .2 diffuse .6 specular 1 roughness .001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.70 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient .15 brilliance 2 diffuse .6 metallic specular 1. roughness .001 reflection .0}
#declare glass = finish {ambient .05 diffuse .3 specular 1. roughness .001}
#declare Rcell = 0.050;
#declare Rbond = 0.100;

#macro atom(LOC, R, COL, FIN)
  sphere{LOC, R texture{pigment{COL} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{COL} finish{FIN}}}
      torus{R, Rcell rotate -45*z texture{pigment{COL} finish{FIN}}}
      translate LOC}
#end

cylinder {< -5.01,  -4.99, -10.00>, <  0.72,  -4.99, -10.00>, Rcell pigment {Black}}
cylinder {< -5.01,   0.73, -10.00>, <  0.72,   0.73, -10.00>, Rcell pigment {Black}}
cylinder {< -5.01,   0.73,   3.75>, <  0.72,   0.73,   3.75>, Rcell pigment {Black}}
cylinder {< -5.01,  -4.99,   3.75>, <  0.72,  -4.99,   3.75>, Rcell pigment {Black}}
cylinder {< -5.01,  -4.99, -10.00>, < -5.01,   0.73, -10.00>, Rcell pigment {Black}}
cylinder {<  0.72,  -4.99, -10.00>, <  0.72,   0.73, -10.00>, Rcell pigment {Black}}
cylinder {<  0.72,  -4.99,   3.75>, <  0.72,   0.73,   3.75>, Rcell pigment {Black}}
cylinder {< -5.01,  -4.99,   3.75>, < -5.01,   0.73,   3.75>, Rcell pigment {Black}}
cylinder {< -5.01,  -4.99, -10.00>, < -5.01,  -4.99,   3.75>, Rcell pigment {Black}}
cylinder {<  0.72,  -4.99, -10.00>, <  0.72,  -4.99,   3.75>, Rcell pigment {Black}}
cylinder {<  0.72,   0.73, -10.00>, <  0.72,   0.73,   3.75>, Rcell pigment {Black}}
cylinder {< -5.01,   0.73, -10.00>, < -5.01,   0.73,   3.75>, Rcell pigment {Black}}
atom(< -5.01,  -4.99,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #0 
atom(< -2.15,  -4.99,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #1 
atom(< -5.01,  -2.13,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #2 
atom(< -2.15,  -2.13,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #3 
atom(< -3.58,  -3.56,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #4 
atom(< -0.72,  -3.56,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #5 
atom(< -3.58,  -0.70,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #6 
atom(< -0.72,  -0.70,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #7 
atom(< -5.01,  -4.97,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #8 
atom(< -2.15,  -5.03,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #9 
atom(< -5.01,  -2.15,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #10 
atom(< -2.15,  -2.09,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #11 
atom(< -2.15,  -3.56,   0.00>, 1.36, rgb <1.00, 0.82, 0.14>, ase3) // #12 
atom(< -5.01,   0.73,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #13 
atom(< -2.15,   0.73,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #14 
atom(< -5.01,   3.60,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #15 
atom(< -2.15,   3.60,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #16 
atom(< -3.58,   2.17,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #17 
atom(< -0.72,   2.17,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #18 
atom(< -3.58,   5.03,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #19 
atom(< -0.72,   5.03,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #20 
atom(< -5.01,   0.76,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #21 
atom(< -2.15,   0.70,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #22 
atom(< -5.01,   3.57,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #23 
atom(< -2.15,   3.64,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #24 
atom(< -2.15,   2.17,   0.00>, 1.36, rgb <1.00, 0.82, 0.14>, ase3) // #25 
atom(<  0.72,  -4.99,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #26 
atom(<  3.58,  -4.99,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #27 
atom(<  0.72,  -2.13,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #28 
atom(<  3.58,  -2.13,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #29 
atom(<  2.15,  -3.56,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #30 
atom(<  5.01,  -3.56,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #31 
atom(<  2.15,  -0.70,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #32 
atom(<  5.01,  -0.70,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #33 
atom(<  0.72,  -4.97,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #34 
atom(<  3.58,  -5.03,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #35 
atom(<  0.72,  -2.15,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #36 
atom(<  3.58,  -2.09,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #37 
atom(<  3.58,  -3.56,   0.00>, 1.36, rgb <1.00, 0.82, 0.14>, ase3) // #38 
atom(<  0.72,   0.73,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #39 
atom(<  3.58,   0.73,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #40 
atom(<  0.72,   3.60,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #41 
atom(<  3.58,   3.60,  -6.00>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #42 
atom(<  2.15,   2.17,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #43 
atom(<  5.01,   2.17,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #44 
atom(<  2.15,   5.03,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #45 
atom(<  5.01,   5.03,  -3.98>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #46 
atom(<  0.72,   0.76,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #47 
atom(<  3.58,   0.70,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #48 
atom(<  0.72,   3.57,  -1.88>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #49 
atom(<  3.58,   3.64,  -2.05>, 1.21, rgb <0.75, 0.65, 0.65>, ase3) // #50 
atom(<  3.58,   2.17,   0.00>, 1.36, rgb <1.00, 0.82, 0.14>, ase3) // #51 
