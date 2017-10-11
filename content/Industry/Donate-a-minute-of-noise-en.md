Title: Donate a Minute of Noise
Date: 2017-10-03 12:00
Author: Gerald Figueras
Tags: engineer; noise; noise supression; voice; voice api; webrtc
Slug: Donate-a-minute-of-noise
Lang: en
Thumbnail: images/after.jpg
Summary: New technology for easily handling noise supression in audio recordings


[The Mozilla Research RRNoise project](https://hacks.mozilla.org/2017/09/rnnoise-deep-learning-noise-suppression/) shows how to apply deep learning to noise suppression. It combines classic signal processing with deep learning, but it’s small and fast. No expensive GPUs required — it runs easily on a Raspberry Pi. The result is easier to tune and sounds better than traditional noise suppression systems.

![noise](/images/after.jpg)

You can try and see the supression results on their [website](https://people.xiph.org/~jm/demo/rnnoise/#music_player) and even try using your own recording to test it. 

RNNoise will help improve the quality of WebRTC calls, especially for multiple speakers in noisy rooms. It is also small enough and fast enough to be executed directly in JavaScript, making it possible for Web developers to embed it directly in Web pages when recording audio.

If you want to help the research, you can donate your own noise. The RRNoise Project website says:

>“If you think this work is useful, there's an easy way to help make it even better! All it takes is a minute of your time. Click on the >link below, to let us record one minute of noise from where you are. This noise can be used to improve the training of the neural >network. As a side benefit, it means that the network will know what kind of noise you have and might do a better job when you get to use >it for videoconferencing (e.g. in WebRTC). We're interested in noise from any environment where you might communicate using voice. That >can be your office, your car, on the street, or anywhere you might use your phone or computer.”

Click here to [donate a minute](https://people.xiph.org/~jm/demo/rnnoise/donate.html) of your noise. 

