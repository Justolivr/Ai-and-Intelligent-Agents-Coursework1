(define (problem lunar-mission-3)
    (:domain lunar-extended)

     (:objects
    ; control rooms, docking bays, waypoints
    wp1 wp2 wp3 wp4 wp5 wp6 - location
    cr1 cr2 - cr
    db1 db2 - db
    
    ; samples to be collected
    sample1 sample2 - sample

    ; data to be collected
    pic1 scan1 pic2 scan2 - data

    ; landers and rovers setup
    lander1 lander2 - lander
    rover1 rover2 - rover

    ; astronaut setup
    alice bob - astronaut
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

    ; connectivity of the lander internal areas
    (connected cr1 db1)
    (connected db1 cr1)
    (connected cr2 db2)
    (connected db2 cr2)

    ; starting points for each astronaut t
    (at alice cr1)
    (at bob cr2)

    ; links between landers, rovers, and astronauts
    (linked lander1 rover1)
    (linked lander2 rover2)
    (astronautLink alice lander1)
    (astronautLink bob lander2)

     ;setup the initial states of the deployed lander1 and rover1 manned by alice
    (deployed rover1)
    (noData rover1)
    (noSample rover1)
    (at rover1 wp2)
    (at lander1 wp2)

    ; lander 2 is manned by bob and initially not landed
    (notLanded lander2)
   

    ; data and sample location setup
    (dataAt pic1 wp3)
    (dataAt scan1 wp4)
    (dataAt pic2 wp2)
    (dataAt scan2 wp6)
    (at sample1 wp5)
    (at sample2 wp1)
    )

    (:goal
        (and


        ; mission goals
        (uploaded pic1) 
        (uploaded scan1)
        (uploaded pic2) 
        (uploaded scan2) 
        (dropped sample1) 
        (dropped sample2) 
        )
    )
)