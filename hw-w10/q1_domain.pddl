(define (domain logistics)
    (:predicates 
        (truck-at-location ?x - location)
        (package-at-location ?x - location ?y - package)
        (package-loaded ?x - package)
    )   

    (:types 
        location package - object
    )

    (:action travel
        :parameters (?from - location ?to - location)
        :precondition (and (truck-at-location ?from))
        :effect (and 
                (truck-at-location ?to) 
            (not 
                (truck-at-location ?from)
            ))    
    )

    (:action load
        :parameters (?location - location ?package - package)
        :precondition (and (truck-at-location ?location) (package-at-location ?location ?package))
        :effect (and 
                    (package-loaded ?package)
                (not 
                    (package-at-location ?location ?package)
                ))
    )    

    (:action unload
        :parameters (?location - location ?package - package)
        :precondition (and (truck-at-location ?location) (package-loaded ?package))
        :effect (and 
                    (package-at-location ?location ?package)
                (not 
                    (package-loaded ?package)
                ))
    )
)
