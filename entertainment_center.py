import media
import fresh_tomatoes



dunkirk = media.Movie("Dunkirk",
                      "Allied soldiers from Belgium, the British Empire and France are surrounded by the German army.",
                      "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker.",
                         "http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_72.jpg",
                         "https://www.youtube.com/watch?v=BdJKm16Co6M")

arrival = media.Movie("Arrival",
                      "When twelve mysterious spacecraft appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien vistors",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=AMgyWT075KY")

the_revenant = media.Movie("The Revenant",
                           "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BY2FmODc2N2QtYmY3MS00YTMwLWI2NGYtZWRmYWVkNjFjZmI0XkEyXkFqcGdeQXVyNTMxMjgxMzA@._V1_.jpg",
                           "https://www.youtube.com/watch?v=QRfj1VCg16Y")

exmachina = media.Movie("Ex Machina",
                        "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=EoQuVnKhxaM")

sicario = media.Movie("Sicario",
                      "an idealistic FBI agent is enlisted by a government task force to aid in the escalating war against drugs at the border area between the U.S. and Mexico",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NjM3NTk1M15BMl5BanBnXkFtZTgwMzg1MzU2NjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=G8tlEcnrGnU")


movies = [dunkirk, fight_club, arrival, the_revenant, exmachina, sicario]
fresh_tomatoes.open_movies_page(movies)
