(define (domain lunar-extended)
    (:requirements :strips :typing)

    (:types
    item
    astronaut sample lander rover - item
    data
    scan pic - data
    location
    db cr - location
    )


  (:predicates 

    ; an item is at a location
    (at ?i - item ?l1 - location)

    ; 2 locations are connected
    (connected ?l1 - location ?l2 - location)

    ; a rover has been deployed from its lander
    (deployed ?r - rover)

    ; a rover has not been deployed by its lander
    (notDeployed ?r - rover)

    ; a rover has a sample s
    (hasSample ?r - rover ?s - sample)

    ; a rover does not have a sample
    (noSample ?r - rover)

    ; a sample has been dropped off at a landesr
    (dropped ?s - sample)

    ; a rover has data
    (hasData ?r - rover ?d - data)
    
    ; a rover has no data
    (noData ?r - rover)

    ; a rover has uploaded data
    (uploaded ?d - data)

    ; data type to be collected a location1
    (dataAt ?d - data ?l1 - location)

    ; a lander and its location
    (landed ?l - lander ?l1 - location)
    
    ; a lander has not landed
    (notLanded ?l - lander)

    ; a rovers link to its lander
    (linked ?l - lander ?r - rover)

    ; an astronauts link to its lander
    (astronautLink ?a - astronaut ?l - lander)
    )

    (:action action_name
        :parameters ()
        :precondition (and)
        :effect (and)
    )

    (:action roverMove
        :parameters (?r - rover ?l1 - location ?l2 - location)
        :precondition (and (at ?r ?l1) (connected ?l1 ?l2) )
        :effect (and (not (at ?r ?l1)) (at ?r ?l2))
    )

    ; move between sections of lander
    (:action astronautMove
        :parameters (?a - astronaut ?l1 - location ?l2 - location)
        :precondition (and (at ?a ?l1) (connected ?l1 ?l2) )
        :effect (and (not (at ?a ?l1)) (at ?a ?l2))
    )

    ; pickup sample
    (:action pickup
        :parameters (?r - rover  ?s - sample ?l1 - location)
        :precondition (and (at ?r ?l1) (at ?s ?l1) (deployed ?r) (noSample ?r) )
        :effect (and (hasSample ?r ?s) (not (at ?s ?l1)) (not (noSample ?r)))
    )

    
    (:action drop
        :parameters (?a - astronaut ?l2 - db ?r - rover ?l - lander ?s - sample ?l1 - location  )
        :precondition (and (at ?r ?l1) (landed ?l ?l1) (deployed ?r) (hasSample ?r ?s) (linked ?l ?r) (at ?a ?l2) (astronautLink ?a ?l))
        :effect (and  (dropped ?s) (noSample ?r))
    )

    ; deploy a rover at a location
    (:action deployRover
        :parameters (?a - astronaut ?l2 - db ?l - lander ?r - rover ?l1 - location  )
        :precondition (and (notDeployed ?r ) (at ?l ?l1)(linked ?l ?r) (at ?a ?l2) (astronautLink ?a ?l))
        :effect (and (at ?r ?l1) (deployed ?r ) (noData ?r) (noSample ?r) (not (notDeployed ?r )) )
    )

    (:action getData
        :parameters (?r - rover ?d - data ?l1 - location)
        :precondition (and (at ?r ?l1) (dataAt ?d ?l1) (deployed ?r) (noData ?r) )
        :effect (and (hasData ?r ?d) (not (dataAt ?d ?l1)) (not (noData ?r)))
    )

    (:action sendData
        :parameters (?a - astronaut ?l2 - cr ?r - rover ?l - lander ?d - data)
        :precondition (and (deployed ?r ) (hasData ?r ?d)(linked ?l ?r) (at ?a ?l2) (astronautLink ?a ?l))
        :effect (and (uploaded ?d)  (noData ?r) )
    )

    (:action land
        :parameters (?l - lander ?r - rover ?l1 - location)
        :precondition (and (notLanded ?l) )
        :effect (and (not (notLanded ?l)) (landed ?l ?l1) (at ?l ?l1) (notDeployed ?r) )
    )

)