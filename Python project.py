#alan arvizu

Media_type = input("Enter media_type: ")

print ("The media type is "+ Media_type)

Genre = input("Enter genre: ")

print ("the genre is " + Genre)

Media_title = input("Enter the title of your selected media: ")

print ("The title of the media is " + Media_title)

Description = input("Enter what you like about the meida: ")

print (Description)

year_created = input("enter the year the media was created: ")

print ("the year the media was ctreated is " + year_created)

Media_rating = float(input("media rating 1/5 = "))

if Media_rating >=4 and Media_rating <=5:

    print(Media_title + " is outstading")

else:

    print(Media_title + " Is Awful")

Media_Review = [Media_type,Genre,Media_title,Description,year_created, Media_rating]

