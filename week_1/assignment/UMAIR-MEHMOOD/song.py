import time


def playSong(song):
    for line in song:
        print(line)
        time.sleep(1)



song = f"""This night is cold in the kingdom
I can feel you fade away
From the kitchen to the bathroom sink and
Your steps keep me awake
Don't cut me down, throw me out, leave me here to waste
I once was a man with dignity and grace
Now I'm slippin' through the cracks of your cold embrace
So please, please
Could you find a way to let me down slowly?
A little sympathy, I hope you can show me
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
Let me down, down, let me down, down, let me down
Let me down, down, let me down, down, let me down
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
Cold skin, drag my feet on the tile
As I'm walking down the corridor
And I know we haven't talked in a while
So I'm looking for an open door
Don't cut me down, throw me out, leave me here to waste
I once was a man with dignity and grace
Now I'm slippin' through the cracks of your cold embrace
So please, please
Could you find a way to let me down slowly?
A little sympathy, I hope you can show me
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
Let me down, down, let me down, down, let me down
Let me down, down, let me down, down, let me down
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
And I can't stop myself from fallin' (down) down
And I can't stop myself from fallin' (down) down
And I can't stop myself from fallin' (down) down
And I can't stop myself from fallin' (down) down
Could you find a way to let me down slowly?
A little sympathy, I hope you can show me
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
Let me down, down, let me down, down, let me down
Let me down, down, let me down, down, let me down
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly"""

song = song.split('\n')
time.sleep(1)
print("song name : Let Me Down Slowly\n")
time.sleep(1)
print("By : Alec Benjamin\n")
time.sleep(1)
playSong(song)