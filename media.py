import webbrowser

#this class sets up the structure of our movie website content in entertainment_center.py
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Args:
            movie_title: Title of the movie.
            movie_storyline: the summary of the movie plot.
            poster_image: link to the image of the movie poster.
            trailer_youtube: link to the youtube trailer.

        """
        self.storyline = movie_storyline
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #function used for opening a youtube video when poster is clicked on
    def show_trailer(self):
        """
        opens the web browser
        """
        webbrowser.open(self.trailer_youtube_url)
