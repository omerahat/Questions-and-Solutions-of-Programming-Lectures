;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ceycey) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
(define str "helloworld")
(define i 5)
(string-append (substring str 0 i) "-" (substring str i))
(circle 100 "solid" "red")
(place-image(circle 100 "solid" "red")10 40(rectangle 200 300 "solid" "green"))
(empty-scene 200 200)
(place-image (circle 100"solid" "red") 10 40 (empty-scene 200 200))
(define myhouse (above(triangle 250 "solid" "brown") (square 250 "solid" "grey")))
(define MYHOUSE(place-image(square 50 "solid" "white" ) 65 300 (place-image (square 50 "solid" "white") 175 300 (place-image (rectangle 60 100 "solid" "white") 120 420 myhouse))))
MYHOUSE
(define mycircle (circle 150 "solid" "green"))
(define x (beside(circle 30 "solid" "red") (circle 30 "solid" "red")))
(overlay (above x x)  mycircle )