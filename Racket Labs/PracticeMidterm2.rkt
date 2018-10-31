;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname PracticeMidterm2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;;a shape is a (make-shape name area color)
;;String name: name of the shape
;;Num area: the area of the shape
;;String Color: the color
(define-struct shape [name area color])

(define circle(make-shape "Circle" 48 "Red"))
(define square(make-shape "Square" 25 "Blue"))
(define circle2(make-shape "Circle" 18 "Green"))

;;A list-of-shapes is either:
;;  - (cons empty)
;;  - (cons list-of-shapes empty)
;;(define (a-list-function a-list)
;;  (cond
;;    [(empty? a-list) empty]
;;    [(cons? a-list)
;;      (cons (first a-list)(a-list-function (rest a-list))))

(define los(list circle square circle2))
(define emptylist(list))

;;sum-circles: list-of-shapes -> Num
;;Consumes: a list of shapes
;;Producces: a sum of the area of the circles in the list
(define (sum-circles los)
  (cond
    [(empty? los) 0]
    [(cons? los) (if
                  (equal? (shape-name (first los)) "Circle")
                  (+ (shape-area (first los)) (sum-circles (rest los)))
                  (sum-circles (rest los)))]))

(check-expect(sum-circles emptylist) 0)
(check-expect(sum-circles los) 66)