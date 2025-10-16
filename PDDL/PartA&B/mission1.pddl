(define (problem lunar-mission-1)
    (:domain lunar)

    ; setup data 
    (:objects
    wp1 wp2 wp3 wp4 wp5 - location
    sample1 - sample
    pic1 scan1 - data
    lander1 - lander
    rover1 - rover
    )

    (:init
    ; location connectivity
    (connected wp1 wp2)
    (connected wp1 wp4)
    (connected wp2 wp3)
    (connected wp3 wp5)
    (connected wp4 wp3)
    (connected wp5 wp1)

    ; lander and rover setup
    (linked lander1 rover1)
    (notLanded lander1)

    ; data and sample setup
    (at sample1 wp1)
    (dataAt pic1 wp5)
    (dataAt scan1 wp3)

    )

    (:goal
        (and
        ; mission goals
        (uploaded pic1)
        (uploaded scan1)
        (dropped sample1)
        
        )
    )
)