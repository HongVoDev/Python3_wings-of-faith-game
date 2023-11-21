from . import imagePathConstants as ipc

"""
This module initializes the dictionary containing assets
and texts relating to the sotryline
"""


story_dict = {
    1: [ipc.bg_1, 'As the flight attendant offers you a'\
            + ' beverage, you notice a fellow passenger'\
            + ' reading a book titled "The Holy Bible."',\
        [2, 'You engage in a conversation about spirituality.', ipc.bg_1a],\
        [3, 'You politely decline and immerse yourself in a book or a movie.', ipc.bg_1b]],\
    
    2: [ipc.bg_2, 'The fellow passenger, John, starts sharing stories of his spiritual journey.',\
        [4, 'You listen attentively and ask thought-provoking questions.', ipc.bg_2a],\
        [3, 'You nod politely but divert the conversation to a different topic.', ipc.bg_2b]],\
    
    3: [ipc.bg_3, 'The flight encounters heavy turbulence, leaving you anxious.',\
        [5, 'You pray silently for strength and peace.', ipc.bg_3a],\
        [6, 'You distract yourself with music or movies to calm your nerves.', ipc.bg_3b]],\

    4: [ipc.bg_4, 'John mentions a church he visited in Vietnam, known for its '\
        +'welcoming community and deep spirituality. He invites you to join him '\
        +'for a service upon arrival.',\
        [7, 'You accept', ipc.bg_4a],\
        [8, 'You express interest but decide to explore the country on your own terms.', ipc.bg_5b]],\

    5: [ipc.bg_5, 'While praying, you feel a sense of calm and reassurance.',\
        [9, 'Your trust in God helps you overcome your fear of turbulence.', ipc.bg_5a],\
        [10, 'Your anxiety escalates, and you struggle to find solace.', ipc.bg_5b]],\

    6: [ipc.bg_6, 'The distractions provide temporary relief, but as the flight progresses, a sense of emptiness creeps in.',\
        [8, 'You reflect on the purpose of life.', ipc.bg_6a],\
        [12, 'You continue to immerse yourself in distractions without seeking deeper meaning.', ipc.bg_6b]],\

    7: [ipc.bg_7, 'You attend the church service with John, where the congregation radiates warmth and acceptance.',\
        [13, 'You engage with the community and participate actively', ipc.bg_7a],\
        [14, 'Feeling overwhelmed, you observe from a distance, resisting the urge to connect.', ipc.bg_7b]],\

    8: [ipc.bg_8, 'As you explore Vietnam independently, you stumble upon a peaceful, tucked-away chapel.',\
        [11, 'You enter and take a moment to reflect.', ipc.bg_8a],\
        [12, 'You choose to focus solely on immersing yourself in the beauty '\
         +'of Vietnam without seeking spiritual experiences.', ipc.bg_8b]],\

    9: [ipc.bg_9, 'As the turbulence subsides, a serene peace engulfs you. Your newfound faith in God '\
        + 'keeps you grounded throughout the flight.'\
        + ' You arrive in Vietnam with a strengthened connection to the Christian god. '\
        + 'Congratulations, you have found God!'],\

    10: [ipc.bg_10, 'The turbulence intensifies, causing panic and fear to grip your heart. Your loss of faith leaves '\
         + 'you feeling vulnerable and lost when you land in Vietnam. Your spiritual journey comes to an end.'],\

    11: [ipc.bg_11, 'As you reflect within the chapel or through independent exploration, deep insights into life\'s '\
         + 'purpose and meaning unfold. Your journey leads you to rediscover faith, connecting to God in a profound way.'],\

    12: [ipc.bg_12, 'Without engaging in self-reflection, your journey becomes shallow and meaningless. '\
         + 'You leave Vietnam with many experiences but fail to connect '\
         + 'with the Christian god. Your spiritual journey comes to an end.'],\

    13: [ipc.bg_13, 'The active engagement with the church community opens doors to meaningful '\
         + 'relationships, spiritual growth, and finding God. Congratulations, you have found God!' ],\

    14: [ipc.bg_14, 'By distancing yourself from the community, you miss out on potential connections. '\
         + 'Feeling isolated, your journey concludes without finding the Christian god. Your spiritual journey comes to an end.']
}
