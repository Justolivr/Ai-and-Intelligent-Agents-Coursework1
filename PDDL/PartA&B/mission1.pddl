(define (problem lunar-mission-1)
    (:domain lunar)

    (:objects
    wp1 wp2 wp3 wp4 wp5 - location
    sample1 - sample
    pic1 scan1 - data
    lander1 - lander
    rover1 - rover
    )

    (:init
    (connected wp1 wp2)
    (connected wp1 wp4)
    (connected wp2 wp3)
    (connected wp3 wp5)
    (connected wp4 wp3)
    (connected wp5 wp1)

    (linked lander1 rover1)

    (notLanded lander1)

    (at sample1 wp1)

    (dataAt pic1 wp5)

    (dataAt scan1 wp3)

    )

    (:goal
        (and
        (uploaded lander1 pic1)
        (uploaded lander1 scan1)
        (dropped lander1 sample1)
        
       
        )
    )
)