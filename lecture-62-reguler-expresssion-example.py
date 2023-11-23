import re

txt = """Once upon a time in the quaint village of Willowbrook, there lived a young girl named Lily. She had an insatiable curiosity that often led her on adventures beyond the village borders. One day, while exploring the dense forest that bordered Willowbrook, abc@gmail.com Lily stumbled upon a mysterious old book hidden beneath the roots of an ancient oak tree.

The book, adorned with intricate symbols, seemed to whisper secrets of forgotten realms. As Lily opened its pages, she found herself transported to a magical world filled krissmoris123@gmail.com with talking animals, enchanted forests, and sparkling lakes. The inhabitants of this realm greeted her warmly, sensing that Lily might be the key to breaking a curse that had shrouded their land in darkness.

Eager to help, Lily hloworld123helo@gmail.com embarked on a quest to find the legendary Crystal of Lumina, the only object that could dispel the shadows. Along the way, she encountered a mischievous fox named Jasper, who became her loyal companion. Together, they faced challenges that tested their wit and courage.

As Lily and Jasper hlokriss@yahoo.in delved deeper into the enchanted world, they discovered that the Crystal of Lumina was guarded by the mythical Phoenix, a majestic creature with fiery plumage. To prove her worthiness, Lily had to solve a series of riddles that moris12kriss@gmail.com would unlock the secret chamber where the crystal was kept.

With determination and the wisdom gained from her journey, Lily successfully solved the riddles, and the Phoenix presented her with the radiant Crystal of Lumina. As she held krissmors12@gamil.in it aloft, the entire realm was bathed in a brilliant light, banishing the shadows and restoring the land to its former glory."""


x = "[a-z]+[0-9]*[a-z]*[@][a-z]+[.][a-z]{2,}"



xyz = re.findall(x, txt)

print(xyz)


