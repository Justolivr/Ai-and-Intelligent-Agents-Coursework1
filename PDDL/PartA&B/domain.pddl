(define (domain lunar)
    (:requirements :strips :typing)

    ; -------------------------------
    ; Types
    ; -------------------------------

    ; EXAMPLE

    ; (:types
    ;     parent_type
    ;     child_type - parent_type

    ; )
    (:types
    item
    sample lander rover - item
    data
    scan pic - data
    location
    )

    ; -------------------------------
    ; Predicates
    ; -------------------------------

    ; EXAMPLE

    ; (:predicates
    ;     (no_arity_predicate)
    ;     (one_arity_predicate ?p - parameter_type)
    ; )

    (:predicates 

    ; an item is at a location
    (at ?i - item ?l1 - location)

    ; 2 locations are connected
    (connected ?l1 - location ?l2 - location)

    ; a rover has been deployed from its lander
    (deployed ?r - rover ?l - lander)

    ; a rover has not been deployed by its lander
    (notDeployed ?r - rover ?l - lander)

    ; a rover has a sample s
    (hasSample ?r - rover ?s - sample)

    ; a rover does not have a sample
    (noSample ?r - rover)

    (dropped ?l - lander ?s - sample)

    ; a rover has data
    (hasData ?r - rover ?d - data)
    
    ; a rover has no data
    (noData ?r - rover)

    ; a rover has uploaded data
    (uploaded ?l - lander ?d - data)

    ; data type to be collected a location1
    (dataAt ?d - data ?l1 - location)

    (landed ?l - lander ?l1 - location)

    (notLanded ?l - lander)

    )



    ; -------------------------------
    ; Actions
    ; -------------------------------

    ; EXAMPLE

    ; (:action action-template
    ;     :parameters (?p - parameter_type)
    ;     :precondition (and
    ;         (one_arity_predicate ?p)
    ;     )
    ;     :effect 
    ;     (and 
    ;         (no_arity_predicate)
    ;         (not (one_arity_predicate ?p))
    ;     )
    ; )

    (:action action_name
        :parameters ()
        :precondition (and)
        :effect (and)
    )

    ; move
     (:action move
        :parameters (?r - rover ?l - lander ?l1 - location ?l2 - location)
        :precondition (and (at ?r ?l1) (connected ?l1 ?l2) (deployed ?r ?l))
        :effect (and (not (at ?r ?l1)) (at ?r ?l2))
    )

    ; pickup sample
    (:action pickup
        :parameters (?r - rover ?l - lander ?s - sample ?l1 - location)
        :precondition (and (at ?r ?l1) (at ?s ?l1) (deployed ?r ?l) (noSample ?r))
        :effect (and (hasSample ?r ?s) (not (at ?s ?l1)) (not (noSample ?r)))
    )

    ; this bit no worky
     (:action drop
        :parameters (?r - rover ?l - lander ?s - sample ?l1 - location)
        :precondition (and (at ?r ?l1) (landed ?l ?l1) (deployed ?r ?l) (hasSample ?r ?s))
        :effect (and  (dropped ?l ?s) (noSample ?r))
    )



    ; deploy a rover at a location
    (:action deployRover
        :parameters (?l - lander ?l1 - location ?r - rover)
        :precondition (and (notDeployed ?r ?l) (at ?l ?l1))
        :effect (and (at ?r ?l1) (deployed ?r ?l) (noData ?r) (noSample ?r) (not (notDeployed ?r ?l)))
    )

    (:action getData
        :parameters (?r - rover ?l - lander ?d - data ?l1 - location)
        :precondition (and (at ?r ?l1) (dataAt ?d ?l1) (deployed ?r ?l) (noData ?r))
        :effect (and (hasData ?r ?d) (not (dataAt ?d ?l1)) (not (noData ?r)))
    )

    (:action sendData
        :parameters (?r - rover ?l - lander ?d - data)
        :precondition (and (deployed ?r ?l) (hasData ?r ?d))
        :effect (and (uploaded ?l ?d)  (noData ?r) )
    )

    (:action land
        :parameters (?l - lander ?r - rover ?l1 - location)
        :precondition (and (notLanded ?l) )
        :effect (and (not (notLanded ?l)) (landed ?l ?l1) (at ?l ?l1) (notDeployed ?r ?l) )
    )

)