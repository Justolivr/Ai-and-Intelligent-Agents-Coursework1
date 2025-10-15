(define (problem lunar-mission-2)
    (:domain lunar)

    (:objects
    wp1 wp2 wp3 wp4 wp5 wp6 - location
    sample1 sample2 - sample
    pic1 scan1 pic2 scan2 - data
    lander1 lander2 - lander
    rover1 rover2 - rover
    )

    (:init
    ; location connectivity
    (connected wp1 wp2)
    (connected wp2 wp1)
    (connected wp2 wp3)
    (connected wp2 wp4)
    (connected wp3 wp5)
    (connected wp4 wp2)
    (connected wp5 wp3)
    (connected wp5 wp6)
    (connected wp6 wp4)

    (linked lander1 rover1)
    (linked lander2 rover2)

    (deployed rover1 lander1)
    (noData rover1)
    (noSample rover1)
    (at rover1 wp2)
    (at lander1 wp2)



    (notLanded lander2)

    (dataAt pic1 wp3)
    (dataAt scan1 wp4)
    (dataAt pic2 wp2)
    (dataAt scan2 wp6)

    (at sample1 wp5)
    (at sample2 wp1)


    )

    (:goal
        (and
        (or (uploaded lander2 pic1) (uploaded lander1 pic1))
        (or (uploaded lander2 scan1) (uploaded lander1 scan1))
        (or (uploaded lander2 pic2) (uploaded lander1 pic2))
        (or (uploaded lander2 scan2) (uploaded lander1 scan2))
        (or (dropped lander2 sample1) (dropped lander1 sample1))
        (or (dropped lander2 sample2) (dropped lander1 sample2))
        )
    )
)