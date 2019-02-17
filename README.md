# SafeLine

_Keeping the elderly safe and connected_

Built with Raspberry Pi, OpenCV, React.js, Firebase, SendGrid API, XCode,
Python, Swift, Javascript

Made by:

- [Cody Enokida](https://github.com/codyenokida)
- [Brandon Khong](https://github.com/brandontkhong)
- [Meta Novitia](https://github.com/metanovitia)
- [Bryon Tjanaka](https://github.com/btjanaka)

Falls are the one of the leading causes of injury for the elderly. Every 11
seconds, an older adult is treated in the emergency room for a fall, and every
19 minutes, an older adult dies from a fall.\* With such shocking statistics,
how could we not help the elderly?

Looking around, we can see that there are already products like Life Alert that
help with falls. However, most of these products are wearable devices, which is
problematic because the elderly may find such products inconvenient to wear.
Sometimes, they may entirely forget to wear the devices. Thus, we decided to
create a method to detect falls and quickly bring assistance to the elderly.

## What it Does

SafeLine uses a Raspberry Pi camera to continuously scan for falls. Once a fall
is detected, SafeLine immediately notifies connected users by sending them an
email and pushing a notification to their iPhones.

## How It Works

SafeLine consists of a number of components. On a Raspberry Pi, we have
connected a camera and used a Python script with OpenCV to continuously check
for falls. Once the script detects someone falling, it uses the SendGrid API to
email a message and an image of the fall to a list of users. It also uploads a
timestamp and the image to Firebase. Firebase also stores the list of emails
for the Python Script. Meanwhile, on each user's iPhones, an iOS app, built
with Swift and XCode, detects that Firebase has been changed. It then
creates the notification and shows it on the user's phone.

Finally, we set up a website on Github pages using React.js. The website is also
registered at [safeline.tech](http://www.safeline.tech)

## Challenges

Along the way, we encountered numerous challenges. Perhaps the biggest challenge
we had was developing the iOS app. None of us has experience with Swift or
XCode, so we struggled to connect the app to Firebase and make it send push
notifications. Another challenge involved improving the sampling rate on the
Raspberry Pi's camera. Since processing images and sending the fall data
requires a lot of computational power, the camera recording was beginning to lag
a lot. Hence, we split the Python script into multiple threads to prevent
separate tasks from interfering with each other. Finally, we found it
challenging to design an appropriate logo and user interface that would
represent our project. To solve this problem, we sought the help of both each
other and the people around us. Overall, we are happy that we were able to
overcome these challenges and connect our entire project.

## What's next for SafeLine?

Here are some of the improvements we could make for SafeLine in the future:

- **Multiple cameras** - we only had one camera for this project, and we would
  certainly like to integrate several, like a real home would have
- **iOS app "friends"** - we could add features such as a "friends list" where
  people can request to watch over someone else, or to have someone else watch
  over them
- **Better accuracy** - the detection algorithm has much room for improvement,
  such as in minimizing the rate of false positives
- **Location detection** - people who are near the person who has fallen can be
  notified, even if they do not specifically monitor that person
- **Sound detection** - on top of image detection, we could learn to recognize
  sounds of falling or cries for help

\*[https://www.aging.com/falls-fact-sheet/](https://www.aging.com/falls-fact-sheet/)
