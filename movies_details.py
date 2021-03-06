import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
					"https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
					"On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
					"https://www.youtube.com/watch?v=6ziBFh3V1aM")

lagaan = media.Movie("LAGAAN",
					"https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
					"The year is 1893 and India is under British occupation. In a small village, the tyrannical Captain Russell (Paul Blackthorne) has imposed an unprecedented land tax on its citizens. Outraged, Bhuvan (Aamir Khan), a rebellious farmer, rallies the villagers to publicly oppose the tax. Russell offers a novel way to settle the dispute: he challenges Bhuvan and his men to a game of cricket, a sport completely foreign to India. If Bhuvan and his men can defeat Russell's team, the tax will be repealed.",
					"https://www.youtube.com/watch?v=6BF-cO1ANc0")

ratatouille = media.Movie("Ratatouille",
					"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
					"Remy dreams of becoming a great chef, despite being a rat in a definitely rodent-phobic profession. He moves to Paris to follow his dream, and with the help of hapless garbage boy Linguini he puts his culinary skills to the test in the kitchen but he has to stay in hiding at the same time, with hilarious consequences. Remy eventually gets the chance to prove his culinary abilities to a great food critic but is the food good? A Pixar animation.",
					"https://www.youtube.com/watch?v=c3sBBRxDAqk")

interstellar = media.Movie("Interstellar",
					"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
					"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
					"https://www.youtube.com/watch?v=8ZCsQfWPZPo")

frozen = media.Movie("Frozen",
					"https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
					"When their kingdom becomes trapped in perpetual winter, fearless Anna (Kristen Bell) joins forces with mountaineer Kristoff (Jonathan Groff) and his reindeer sidekick to find Anna's sister, Snow Queen Elsa (Idina Menzel), and break her icy spell. Although their epic journey leads them to encounters with mystical trolls, a comedic snowman (Josh Gad), harsh conditions, and magic at every turn, Anna and Kristoff bravely push onward in a race to save their kingdom from winter's cold grip.",
					"https://www.youtube.com/watch?v=TbQm5doF_Uc")

the_martian = media.Movie("The Martian",
					"https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
					"When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon), presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet. Meanwhile, back on Earth, members of NASA and a team of international scientists work tirelessly to bring him home, while his crew mates hatch their own plan for a daring rescue mission.",
					"https://www.youtube.com/watch?v=Ue4PCI0NamI")


#frozen.show_trailer()
#avatar.show_poster()
#print (lagaan.storyline)
#------------------------------------------------------------------------------------------------------------------
movie_list = [avatar,ratatouille,lagaan,the_martian,frozen,interstellar]
website = fresh_tomatoes.open_movies_page(movie_list)
print website