Title: OASIS - An Attempt to Automate Optical SETI
Date: 2019-09-09
Category: Astronomy
Author: Andrew Stewart
Summary: Building an image processing pipeline in Python to subtract astronomical images from each other and detect transient events.
Tags: Astronomy, Python, Image Processing, Optical SETI

# Question
Assuming that difference imaging is a viable method for detecting transient events of a ETI-nature, can I build a pipeline in Python to make this process accurate and efficient?
# Methodology
Here's what I tried. It should be known that when I started this project, I was hardly much of a programmer, and even "hardlier" a SETI researcher. 
I really knew very little about what I was doing. But as these things go, it was a great learning opportunity.
### Background
Before getting into the details, I'll quickly set the scene. It's 2016. I'm in my Sophomore year of college, and I was looking for a research project to undertake in the Summer. I had family in Santa Barbara, and knew
how well-regarded UCSB's Physcis department was, so I looked into their active labs to find one that was doing something interesting.  
The [Experimental Cosmology Group](https://www.deepspace.ucsb.edu/){:target="_blank"} was the first to catch my eye. They had a number of active projects in the works that seemed to combine both experimental and theoretical work quite nicely.
As a student who really didn't know what he wanted to do, this breadth was attractive.
I reached out to Philip Lubin, the group's PI, and unlike most professors receiving a cold email from a undergrad Physics student, he responded quickly and set up a phone call.
For such an established scientist, he was ridiculously patient and devoted when it came to education and outreach. He invited me to work on a SETI project for the summer, as there wasn't anybody focused on it at the time.  
Again, it can't be overstated how unusual and cool this was. Few researchers would take the time to mentor a student from another college, with little experience, and give them access to their lab resources and group members.
This was a fantastic opportunity, and I'll always be thankful to Dr. Lubin for facilitating it.
### The Project
Okay, what was this SETI project all about?  
Fundamentally, the focus of the SETI team at the Experimental Cosmology Group has been on *Optical SETI*. This is the branch of SETI
dealing with the search for signals (and at times the broadcast of our own signals) in the optical range of the EM spectrum.  
Optical SETI is, even in 2025, still relatively fringe with respect to the more popular SETI methods that search and broadcast in the longer wavelengths (think the classic arrays of radio telescope a la "Contact"). There are many reasons for this, mostly historical, and the story is interesting. There are lots of articles out there if you want to learn more, I won't go into it here.  
Anyway, optical SETI searches can largely be split into two groups: pulsed and continuous. Pulsed involves looking for extremely short (temporally) burst of light coming from an observed source.
Pulsed searches are the more popular of the two because of the advantageous signal-to-noise ratio involved. Modern lasers are capable of producing extremely short pulses of light, on the nanosecond scale. In nature, however, significant signals in this time range are rare, making detection relatively straightforward. Lots of cool work has been done on pulsed searches.  
But maybe an extraterrestrial civilization doesn't send a nanosecond pulsed signal. Maybe they instead output a directed, continuous beam of light. This kind of signal would be much harder to detect with the equipment and software used in the pulsed surveys.  
Enter this project - a search for optical, continuous signal from an extraterrestrial civilization. Much of the theoretical ground-work was laid in [Dr. Lubin's original paper on the subject](http://wedge.deepspace.ucsb.edu/wordpress/wp-content/uploads/2015/04/SDI-u2.pdf){:target="_blank"}. The work I completed really just attempted to use some software and data to test the ideas that Lubin already had posited.  
  
Lubin's basic idea was this - what if some ETI broadcasted a powerful, continuous wave laser signal in our direction? How would we go about detecting it? There are lots of possible answers to this question, but the one we tried to implement was the idea of apply *difference imaging* on densely populated sky survey data.  
Difference imaging is a very simple concept, and is exactly what it sounds like. If you want to detect something in an image that wasn't there before, you take two images of the same field of view and subtract them from each other. If the images are perfectly aligned, the only thing that will remain in the subtracted image is, hopefully, the signal you're after.
This is one of those techniques that seems *so* simple, but yet is very tricky to get working in practice.  
  
OASIS, the image processing pipeline I built, was an attempt to make this difference imaging technique viable.



# Results

# Takeaways
Like anything, this project had good and bad.
# Looking Forward
# Resources
