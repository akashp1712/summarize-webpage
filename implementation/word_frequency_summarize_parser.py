# -*- coding: utf-8 -*-
# Implementation from https://dev.to/davidisrawi/build-a-quick-summarizer-with-python-and-nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from framework.parser.parser import Parser

text_str = '''
<header>My name is Wil Wheaton. I Live With Chronic Depression and Generalized Anxiety. I Am Not Ashamed.</header><p>Before I begin, I want to warn you that this talk touches on many triggering subjects, including self-harm and suicide. I also want you to know that I’m speaking from my personal experience, and that if you or someone you know may be living with mental illness, please talk to a licensed and qualified medical professional, because I am not a doctor.</p><p>Okay, let’s do this.</p><p>Hi, I’m Wil Wheaton. I’m 45 years-old, I have a wonderful wife, two adult children who make me proud every day, and a daughter in-law who I love like she’s my own child. I work on the most popular comedy series in the world, I’ve been a New York Times Number One Bestselling Audiobook narrator, I have run out of space in my office for the awards I’ve received for my work, and as a white, heterosexual, cisgender man in America, I live life on the lowest difficulty setting — with the Celebrity cheat enabled.</p><p><b>My life is, by every objective measurement, very very good.</b></p><p><b>And in spite of all of that, I struggle every day with my self esteem, my self worth, and my value not only as an actor and writer, but as a human being.</b></p><p>That’s because I live with Depression and Anxiety, the tag team champions of the World Wrestling With Mental Illness Federation.</p><p>And I’m not ashamed to stand here, in front of six hundred people in this room, and millions more online, and proudly say that I live with mental illness, and that’s okay. I say “with” because even though my mental illness tries its best, it doesn’t control me, it doesn’t define me, and I refuse to be stigmatized by it.</p><p><b>So. My name is Wil Wheaton, and I have Chronic Depression.</b></p><p>It took me over thirty years to be able to say those ten words, and I suffered for most of them as a result. I suffered because though we in America have done a lot to help people who live with mental illness, we have not done nearly enough to make it okay for our fellow travelers on the wonky brain express to reach out and accept that help.</p><p>I’m here today to talk with you about working to end the stigma and prejudice that surrounds mental illness in America, and as part of that, I want to share my story with you.</p><p>When I was a little kid, probably seven or eight years old, I started having panic attacks. Back then, we didn’t know that’s what they were, and because they usually happened when I was asleep, the adults in my life just thought I had nightmares. Well, I did have nightmares, but they were so much worse than just bad dreams. Night after night, I’d wake up in absolute terror, and night after night, I’d drag my blankets off my bed, to go to sleep on the floor in my sister’s bedroom, because I was so afraid to be alone.</p><p>There were occasional stretches of relief, sometimes for months at a time, and during those months, I felt like what I considered to be a normal kid, but the panic attacks always came back, and each time they came back, they seemed worse than before.</p><p>When I was around twelve or thirteen, my anxiety began to express itself in all sorts of delightful ways.</p><p>I worried about everything. I was tired all the time, and irritable most of the time. I had no confidence and terrible self-esteem. I felt like I couldn’t trust anyone who wanted to be close to me, because I was convinced that I was stupid and worthless and the only reason anyone would want to be my friend was to take advantage of my fame.</p><p>This is important context. When I was thirteen, I was in an internationally-beloved film called Stand by Me, and I was famous. Like, really famous, like, can’t-go-to-the-mall-with-my-friends-without-getting-mobbed famous, and that meant that all of my actions were scrutinized by my parents, my peers, my fans, and the press. All the weird, anxious feelings I had all the time? I’d been raised to believe that they were shameful. That they reflected poorly on my parents and my family. That they should be crammed down deep inside me, shared with nobody, and kept secret.</p><p>My panic attacks happened daily, and not just when I was asleep. When I tried to reach out to the adults in my life for help, they didn’t take me seriously. When I was on the set of a tv show or commercial, and I was having a hard time breathing because I was so anxious about making a mistake and getting fired? The directors and producers complained to my parents that I was being difficult to work with. When I was so uncomfortable with my haircut or my crooked teeth and didn’t want to pose for teen magazine photos, the publicists told me that I was being ungrateful and trying to sabotage my success. When I couldn’t remember my lines, because I was so anxious about things I can’t even remember now, directors would accuse me of being unprofessional and unprepared. And that’s when my anxiety turned into depression.</p><header>(I’m going to take a moment for myself right now, and I’m going to tear a hole in the fabric of spacetime and I’m going to tell all those adults from the past: give this kid a break. He’s scared. He’s confused. He is doing the best he can, and if you all could stop seeing him as a way to put money into your pockets, maybe you could see that he’s suffering and needs help.)</header><p>I was miserable a lot of the time, and it didn’t make any sense. I was living a childhood dream, working on Star Trek: The Next Generation, and getting paid to do what I loved. I had all the video games and board games I ever wanted, and did I mention that I was famous?</p><p>I struggled to reconcile the facts of my life with the reality of my existence. I knew something was wrong with me, but I didn’t know what. And because I didn’t know what, I didn’t know how to ask for help.</p><p>I wish I had known that I had a mental illness that could be treated! I wish I had known that that the way I felt wasn’t normal and it wasn’t necessary. I wish I had known that I didn’t deserve to feel bad, all the time.</p><p>And I didn’t know those things, because Mental Illness was something my family didn’t talk about, and when they did, they talked about it like it was something that happened to someone else, and that it was something they should be ashamed of, because it was a result of something they did. This prejudice existed in my family in spite of the ample incidence of mental illness that ran rampant through my DNA, featuring successful and unsuccessful suicide attempts by my relations, more than one case of bipolar disorder, clinical depression everywhere, and, because of self-medication, so much alcoholism, it was actually notable when someone didn’t have a drinking problem.</p><p>Now, I don’t blame my parents for how they addressed — or more accurately didn’t address — my mental illness, because I genuinely believe they were blind to the symptoms I was exhibiting. They grew up and raised me in the world I’ve spent the last decade of my life trying to change. They lived in a world where mental illness was equated with weakness, and shame, and as a result, I suffered until I was in my thirties.</p><p>And it’s not like I never reached out for help. I did! I just didn’t know what questions to ask, and the adults I was close to didn’t know what answers to give.</p><p>Mom, I know you’re going to read this or hear this and I know it’s going to make you upset. I want you to know that I love you, and I know that you did the very best you could. I’m telling my story, though, so someone else’s mom can see the things you didn’t, through no fault of your own.</p><p>I clearly remember being twenty-two, living in my own house, waking up from a panic attack that was so terrifying just writing about it for this talk gave me so much anxiety I almost cut this section from my speech. It was the middle of the night, and I drove across town, to my parents’ house, to sleep on the floor of my sister’s bedroom again, because at least that’s where I felt safe. The next morning, I tearfully asked my mom what was wrong with me. She knew that many of my blood relatives had mental illness, but she couldn’t or wouldn’t connect the dots. “You’re just realizing that the world is a scary place,” she said.</p><p>Yeah, no kidding. The world terrifies me every night of my life and I don’t know why or how to stop it.</p><p>Again, I don’t blame her and neither should you. She really was doing the best that she could for me, but stigma and the shame is inspires are powerful things.</p><p>I want to be very clear on this: Mom, I know you’re going to read this or hear this and I know it’s going to make you upset. I want you to know that I love you, and I know that you did the very best you could. I’m telling my story, though, so someone else’s mom can see the things you didn’t, through no fault of your own.</p><p>Through my twenties, I continued to suffer, and not just from nightmares and panic attacks. I began to develop obsessive behaviors that I’ve never talked about in public until right now. Here’s a very incomplete list: I began to worry that the things I did would affect the world around me in totally irrational ways. I would hold my breath underneath bridges when I was driving, because if I didn’t, maybe I’d crash my car. I would tap the side of an airplane with my hand while I was boarding, and tell it to take care of me when I flew places for work, because I was convinced that if I didn’t, the plane would crash. Every single time I said goodbye to someone I cared about, my brain would play out in vivid detail how I would remember this as the last time I saw them. Talking about those memories, even without getting into specifics, is challenging. It’s painful to recall, but I’m not ashamed, because all those thoughts — which I thankfully don’t have any more, thanks to medical science and therapy — were not my fault any more than the allergies that clog my sinuses when the trees in my neighborhood start doin’ it every spring are my fault. It’s just part of who I am. It’s part of how my brain is wired, and because I know that, I can medically treat it, instead of being a victim of it.</p><p>One of the primary reasons I speak out about my mental illness, is so that I can make the difference in someone’s life that I wish had been made in mine when I was young, because not only did I have no idea what Depression even was until I was in my twenties, once I was pretty sure that I had it, I suffered with it for another fifteen years, because I was ashamed, I was embarrassed, and I was afraid.</p><p>So I am here today to tell anyone who can hear me: if you suspect that you have a mental illness, there is no reason to be ashamed, or embarrassed, and most importantly, you do not need to be afraid. You do not need to suffer. There is nothing noble in suffering, and there is nothing shameful or weak in asking for help. This may seem really obvious to a lot of you, but it wasn’t for me, and I’m a pretty smart guy, so I’m going to say it anyway: There is no reason to feel embarrassed when you reach out to a professional for help, because the person you are reaching out to is someone who has literally dedicated their life to helping people like us live, instead of merely exist.</p><p>I missed out on a lot of things, during what are supposed to be the best years of my life, because I was paralyzed by What If-ing anxiety.</p><p>That difference, between existing and living, is something I want to focus on for a minute: before I got help for my anxiety and depression, I didn’t truly live my life. I wanted to go do things with my friends, but my anxiety always found a way to stop me. Traffic would just be too stressful, it would tell me. It’s going to be a real hassle to get there and find parking, it would helpfully observe. And if those didn’t stop me from leaving my house, there was always the old reliable: What if…? Ah, “What if… something totally unlikely to happen actually happens? What if the plane crashes? What if I sit next to someone who freaks me out? What if they laugh at me? What if I get lost? What if I get robbed? What if I get locked out of my hotel room? What if I slip on some ice I didn’t see? What if there’s an earthquake? What if what if what if what if…</p><p>When I look back on most of my life, it breaks my heart that when my brain was unloading an endless pile of what ifs on me, it never asked, “What if I go do this thing that I want to do, and it’s … fun? What if I enjoy myself, and I’m really glad I went?”</p><p>I have to tell you a painful truth: I missed out on a lot of things, during what are supposed to be the best years of my life, because I was paralyzed by What If-ing anxiety.</p><p>All the things that people do when they are living their lives … all those experiences that make up a life, my anxiety got in between me and doing them. So I wasn’t living. I was just existing.</p><p>And through it all, I never stopped to ask myself if this was normal, or healthy, or even if it was my fault. I just knew that I was nervous about stuff, and I worried a lot. For my entire childhood, my mom told me that I was a worry wart, and my dad said I was overly dramatic about everything, and that’s just the way it was.</p><p>Except it didn’t have to be that way, and it took me having a full blown panic attack and a complete meltdown at Los Angeles International Airport for my wife to suggest to me that I get help.</p><p>Like I said, I had suspected for years that I was clinically depressed, but I was afraid to admit it, until the most important person in my life told me without shame or judgment that she could see that I was suffering. So I went to see a doctor, and I will never forget what he said, when I told him how afraid I was: “Please let me help you.”</p><p>I think it was then, at about 34 years-old, that I realized that Mental Illness is not weakness. It’s just an illness. I mean, it’s right there in the name “Mental ILLNESS” so it shouldn’t have been the revelation that it was, but when the part of our bodies that is responsible for how we perceive the world and ourselves is the same part of our body that is sick, it can be difficult to find objectivity or perspective.</p><p>So I let my doctor help me. I started a low dose of an antidepressant, and I waited to see if anything was going to change.</p><p>And boy did it.</p><p>My wife and I were having a walk in our neighborhood and I realized that it was just a really beautiful day — it was warm with just a little bit of a breeze, the birds sounded really beautiful, the flowers smelled really great and my wife’s hand felt really good in mine.</p><p>And as we were walking I just started to cry and she asked me, “what’s wrong?”</p><p>I said “I just realized that I don’t feel bad and I just realized that I’m not existing, I’m living.”</p><p>At that moment, I realized that I had lived my life in a room that was so loud, all I could do every day was deal with how loud it was. But with the help of my wife, my doctor, and medical science, I found a doorway out of that room.</p><p>I had taken that walk with my wife almost every day for nearly ten years, before I ever noticed the birds or the flowers, or how loved I felt when I noticed that her hand was holding mine. Ten years — all of my twenties — that I can never get back. Ten years of suffering and feeling weak and worthless and afraid all the time, because of the stigma that surrounds mental illness.</p><p>I’m not religious, but I can still say Thank God for Anne Wheaton. Thank God for her love and support. Thank God that my wife saw that I was hurting, and thank God she didn’t believe the lie that Depression is weakness, or something to be ashamed of. Thank God for Anne, because if she hadn’t had the strength to encourage me to seek professional help, I don’t know how much longer I would have been able to even exist, to say nothing of truly living.</p><p>I started talking in public about my mental illness in 2012, and ever since then, people reach out to me online every day, and they ask me about living with depression and anxiety. They share their stories, and ask me how I get through a bad day, or a bad week.</p><header>Right now, there is a child somewhere who has the same panic attacks I had, and their parents aren’t getting them help, because they believe it reflects poorly on their parenting to have a child with mental illness.</header><p>Here’s one of the things I tell them:</p><p>One of the many delightful things about having Depression and Anxiety is occasionally and unexpectedly feeling like the whole goddamn world is a heavy lead blanket, like that thing they put on your chest at the dentist when you get x-rays, and it’s been dropped around your entire existence without your consent.</p><p>Physically, it weighs heavier on me in some places than it does in others. I feel it tugging at the corners of my eyes, and pressing down on the center of my chest. When it’s really bad, it can feel like one of those dreams where you try to move, but every step and every motion feels like you’re struggling to move through something heavy and viscous. Emotionally, it covers me completely, separating me from my motivation, my focus, and everything that brings me joy in my life.</p><p>When it drops that lead apron over us, we have to remind ourselves that one of the things Depression does, to keep itself strong and in charge, is tell us lies, like: I am the worst at everything. Nobody really likes me. I don’t deserve to be happy. This will never end. And so on and so on. We can know, in our rational minds, that this is a giant bunch of bullshit (and we can look at all these times in our lives when were WERE good at a thing, when we genuinely felt happy, when we felt awful but got through it, etc.) but in the moment, it can be a serious challenge to wait for Depression to lift the roadblock that’s keeping us from moving those facts from our rational mind to our emotional selves.</p><p>And that’s the thing about Depression: we can’t force it to go away. As I’ve said, if I could just “stop feeling sad” I WOULD. (And, also, Depression isn’t just feeling sad, right? It’s a lot of things together than can manifest themselves into something that is most easily simplified into “I feel sad.”)</p><p>So another step in our self care is to be gentle with ourselves. Depression is beating up on us already, and we don’t need to help it out. Give yourself permission to acknowledge that you’re feeling terrible (or bad, or whatever it is you are feeling), and then do a little thing, just one single thing, that you probably don’t feel like doing, and I PROMISE you it will help. Some of those things are:</p><ul><li>Take a shower. </li><li>Eat a nutritious meal. </li><li>Take a walk outside (even if it’s literally to the corner and back). </li><li>Do something — throw a ball, play tug of war, give belly rubs — with a dog. Just about any activity with my dogs, even if it’s just a snuggle on the couch for a few minutes, helps me. </li><li>Do five minutes of yoga stretching. </li><li>Listen to a guided meditation and follow along as best as you can. </li></ul><p>Finally, please trust me and know that this shitty, awful, overwhelming, terrible way you feel IS NOT FOREVER. It will get better. It always gets better. You are not alone in this fight, and you are OK.</p><p>No person anywhere, especially here in the richest country in the world, should live in the shadows or suffer alone, because they can’t afford treatment. We have all the money in the world for weapons and corporate tax cuts, so I know that we can afford to prioritize not just health care in general, but mental health care, specifically.</p><p>Right now, there is a child somewhere who has the same panic attacks I had, and their parents aren’t getting them help, because they believe it reflects poorly on their parenting to have a child with mental illness. Right now, there is a teenager who is contemplating self harm, because they don’t know how to reach out and ask for help. Right now, there are too many people struggling just to get to the end of the day, because they can’t afford the help that a lot of us can’t live without. But there are also people everywhere who are picking up the phone and making an appointment. There are parents who have learned that mental illness is no different than physical illness, and they’re helping their children get better. There are adults who, like me, were terrified that antidepressant medication would make them a different person, and they’re hearing the birds sing for the first time, because they have finally found their way out of the dark room.</p><p>I spent the first thirty years of my life trapped in that dark, loud room, and I know how hopeless and suffocating it feels to be in there, so I do everything I can to help others find their way out. I do that by telling my story, so that my privilege and success does more than enrich my own life. I can live by example for someone else the way Jenny Lawson lives by example for me.</p><p>But I want to leave you today with some suggestions for things that we can all do, even if you’re not Internet Famous like I am, to help end the stigma of mental illness, so that nobody has to merely exist, when they could be living.</p><p>We can start by demanding that our elected officials fully fund mental health programs. No person anywhere, especially here in the richest country in the world, should live in the shadows or suffer alone, because they can’t afford treatment. We have all the money in the world for weapons and corporate tax cuts, so I know that we can afford to prioritize not just health care in general, but mental health care, specifically.</p><p>And until our elected officials get their acts together, we can support organizations like NAMI, that offer low and no-cost assistance to anyone who asks for it. We can support organizations like Project UROK, that work tirelessly to end stigmatization and remind us that we are sick, not weak.</p><p>We can remember, and we can remind each other, that there is no finish line when it comes to mental illness. It’s a journey, and sometimes we can see the path we’re on all the way to the horizon, while other times we can’t even see five feet in front of us because the fog is so thick. But the path is always there, and if we can’t locate it on our own, we have loved ones and doctors and medications to help us find it again, as long as we don’t give up trying to see it.</p><p>Finally, we who live with mental illness need to talk about it, because our friends and neighbors know us and trust us. It’s one thing for me to stand here and tell you that you’re not alone in this fight, but it’s something else entirely for you to prove it. We need to share our experiences, so someone who is suffering the way I was won’t feel weird or broken or ashamed or afraid to seek treatment. So that parents don’t feel like they have failed or somehow screwed up when they see symptoms in their kids.</p><p>People tell me that I’m brave for speaking out the way I do, and while I appreciate that, I don’t necessarily agree. Firefighters are brave. Single parents who work multiple jobs to take care of their kids are brave. The Parkland students are brave. People who reach out to get help for their mental illness are brave. I’m not brave. I’m just a writer and occasional actor who wants to share his privilege and good fortune with the world, who hopes to speak out about mental health so much that one day, it will be wholly unremarkable to stand up and say fifteen words:</p><p>My name is Wil Wheaton, I live with chronic depression, and I am not ashamed.</p>
'''

# All weightage for structure doc
# Important: These scores are for the experimenting purpose only
WEIGHT_FOR_LIST = 5
WEIGHT_FOR_HIGHLIGHTED = 10
WEIGHT_FOR_NUMERICAL = 5
WEIGHT_FIRST_PARAGRAPH = 5
WEIGHT_BASIC = 1


def _create_frequency_table(paragraph_list) -> dict:
    """
    we create a dictionary for the word frequency table.
    For this, we should only use the words that are not part of the stopWords array.

    Removing stop words and making frequency table
    Stemmer - an algorithm to bring words to its root word.
    :rtype: dict
    """
    stopWords = set(stopwords.words("english"))

    ps = PorterStemmer()

    freqTable = dict()
    for paragraph in paragraph_list:
        words = word_tokenize(paragraph.text)

        all_highlighted_sentences = [sent for sent in paragraph.get_highlighted()]
        highlighted_words_text = " ".join(all_highlighted_sentences)
        highlighted_words = word_tokenize(highlighted_words_text)

        for word in words:

            if paragraph.is_list_set:
                weight = WEIGHT_FOR_LIST
            else:
                weight = WEIGHT_BASIC

            if word in highlighted_words:
                weight += WEIGHT_FOR_HIGHLIGHTED

            if word.isnumeric() and len(word) >= 2:
                weight += WEIGHT_FOR_NUMERICAL

            if paragraph.is_first_paragraph:
                weight += WEIGHT_FIRST_PARAGRAPH

            word = ps.stem(word)
            if word in stopWords:
                continue

            if word in freqTable:
                freqTable[word] += weight
            else:
                freqTable[word] = weight

    return freqTable


def _score_sentences(sentences, freqTable) -> dict:
    """
    score a sentence by its words
    Basic algorithm: adding the frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """
    # TODO: Can you make this multiprocess compatible in python?

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

        '''
        Notice that a potential issue with our score algorithm is that long sentences will have an advantage over short sentences. 
        To solve this, we're dividing every sentence score by the number of words in the sentence.
        
        Note that here sentence[:10] is the first 10 character of any sentence, this is to save memory while saving keys of
        the dictionary.
        '''

    return sentenceValue


def _find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    average = 0
    # Average value of a sentence from original summary_text
    if len(sentenceValue) > 0:
        average = (sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    # TODO: check if the sentences in the summarization is in the original order of occurrence.

    return summary


def run_summarization(paragraph_list):
    # 1 Create the word frequency table
    freq_table = _create_frequency_table(paragraph_list)
    # print (freq_table)

    '''
    We already have a sentence tokenizer, so we just need 
    to run the sent_tokenize() method to create the array of sentences.
    '''

    # 2 Tokenize the sentences
    sentences = [paragraph.text for paragraph in paragraph_list]
    # print(sentences)

    # 3 Important Algorithm: score the sentences
    sentence_scores = _score_sentences(sentences, freq_table)

    # 4 Find the threshold
    threshold = _find_average_score(sentence_scores)

    # 5 Important Algorithm: Generate the summary
    summary = _generate_summary(sentences, sentence_scores, 1.3 * threshold)

    return summary


if __name__ == '__main__':
    parser = Parser()
    parser.feed(text_str)
    result = run_summarization(parser.paragraphs)
    print(result)
