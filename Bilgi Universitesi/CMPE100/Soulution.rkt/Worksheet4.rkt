;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ödevv) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp") (lib "universe.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp") (lib "universe.rkt" "teachpack" "2htdp")) #f)))
;data definition:number
;purpose:to calculate fahrenheit degree
;contract:number(Celsius degree)--> number(fahrenheit degree)
;example:
(check-expect(fromCeltoFahr 20)68)
(check-expect(fromCeltoFahr 35)95)
;function header:
;(define(fromCeltoFahr x) y)
;template:
;(define(fromCeltoFahr x) (....x...))
;function:
(define(fromCeltoFahr x)(+ (* x 1.8) 32))
  (fromCeltoFahr 62)
;---------------------------------------------------------

;data definition:number
;purpose:to calculate area of rectangle
;contract:number(width) number(height)--> umber(area of rectangle)
;example:
(check-expect(areaOfRect 4 5)20)
(check-expect(areaOfRect 8 5)40)
;function header:
;(define(areaOfRect x y )0)
;template:
;(define (areOfRect)(..x..y..))
;fuction:
(define(areaOfRect x y)(* x y))
(areaOfRect 7 12)
;------------------------------------------------

;data definition:number
;purpose: to draw rectangle
;contract:number(width) number(height)--> image(rectagle)
;example:
(check-expect (drawRect 10 30) (rectangle 10 30 "solid" "blue"))
;function header:
;(define(drawRect x y)myRect)
;template:
;(define(drawRect x y) (...x..y...)
;function:
(define(drawRect x y)  (rectangle x y "solid" "blue"))
(drawRect 20 30)
;------------------------------------------------
;data definition:number
;purpose: to calculate BMI
;contract: number(weight)number(height)-->number(BMI)
;example;
(check-expect ( calculateBMI 72 1.50) 32)
;function header:
;define(calculateBMI x y ) 0)
;template:
;(define(calculateBMI x y) (...x...y..))
;funtion:
(define(calculateBMI x y) (/ x (sqr y)))
  (calculateBMI 50 1.75)
;-----------------------------------------------
;data definition:number
;purpose? to fly ufo
;contract:
