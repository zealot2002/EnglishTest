import random
import numpy as np  

dict1 = {
        "Absolutely.":"是这样;当然是;正是如此;绝对如此。",

        "Absolutely impossible!":"绝对不可能的!",

        "All I have to do is learn English.":"我所要做的就是学英语。",
         
        "Are you free tomorrow?":"你明天有空吗?",
         
        "Are you married?":"你结婚了吗?",
         
        "Are you used to the food here?":" 你习惯吃这儿的饭菜吗?",
         
        "Be careful.":" 小心、注意。",
         
        "Be my guest.":" 请便、别客气。",
         
        "Better late than never.":" 迟到总比不做好。",
         
        "Better luck next time.":" 祝你下一次好运。",
         
        "Better safe than sorry.":" 小心不出大错。",
         
        "Can I have a day off?":" 我能请一天假吗?",
         
        "Can I help?":" 要我帮忙吗?",
         
        "Can I take a message?":" 要我传话吗?",
         
        "Can I take a rain check?":" 你能改天再请我吗?",
         
        "Can I take your order?":" 您要点菜吗?",
         
        "Can you give me a wake-up call?":" 你能打电话叫醒我吗?",
         
        "Could you give me some advice?":" 你能给我一些建议吗?",
         
        "Can you make it?":" 你能来吗?",
         
        "Can I have a word with you?":" 我能跟你谈一谈吗?",
         
        "Catch me later.":" 过会儿再来找我。",
         
        "Cheer up!":" 高兴起来!振作起来! ",

        "Come in and make yourself at home.":" 请进,别客气。",
         
        "Could I have the bill, please?":" 请把账单给我好吗?",
         
        "Could you drop me off at the airport?":" 你能载我到飞机场吗?",
         
        "Could you speak slower?":" 你能说得慢一点吗?",
         
        "Could you take a picture for me?":" 你能帮我拍照吗?",
         
        "Did you enjoy your flight?":" 你的飞行旅途愉快吗?",
         
        "Did you have a good day today?":" 你今天过得好吗?",
         
        "Did you have a nice holiday?":" 你假期过得愉快吗?",
         
        "Did you have fun?":" 你玩得开心吗?",
         
        "Dinner is on me.":" 晚饭我请客。",
         
        "Do you have a room available?":" 你们有空房间吗?",
         
        "Do you have any hobbies?":" 你有什么爱好吗?",
         
        "Do you have some change?":" 你有零钱吗?",
         
        "Do you mind my smoking?":" 你介意我抽烟吗?",
         
        "Do you often work out?":" 你经常锻炼身体吗?",
         
        "Do you speak English?":" 你会说英语吗?",
         
        "Don't be so modest.":" 别这么谦虚。",
         
        "Don't bother.":" 不用麻烦了。",
         
        "Don't get me wrong.":" 别误会我。",
         
        "Don't give up.":" 别放弃。",
         
        "Don't jump to conclusions.":" 不要急于下结论。",
         
        "Don't let me down.":" 别让我失望。",
         
        "Don't make any mistakes.":" 别出差错。",
         
        "Don't mention it.":"别提了",
         
        "Don't miss the boat.":" 不要坐失良机。",
         
        "Don't take any chances.":" 不要心存侥幸。",
         
        "Don't take it for granted.":" 不要想当然。",
         
        "Don't worry about it.":" 别担心。",

        }

dict2 = {
         
        "Easy come, easy go.":"来得容易，去得快。",
         
        "Enjoy your meal.":" 请慢慢享用吧。",
         
        "Easier said than done.":" 说明容易做时难。",
         
        "First come, first served.":" 捷足先登。",
         
        "For here or to go?":" 在这儿吃还是带走?",
         
        "Forget it.":" 算了吧。",
         
        "Forgive me.":" 请原谅我。",
         
        "Give me a call.":" 给我打电话。",
         
        "Give my best to your family.":" 代我向你们全家问好。",

        "Have him return my call.":" 让他给我回电话。",
         
        "Have you ever been to China?":" 你去过中国吗?",
         
        "Have you finished it?":" 你做完了吗?",
         
        "Have you got anything larger?":" 有大一点儿的吗?",
         
        "Have you got that?":" 你明白我的意思吗?",
         
        "Have you heard from Mary?":" 你收到玛丽的来信吗? ",

        "He is in conference.":" 他正在开会。",
         
        "Help yourself, please.":" 请自己用。",
         
        "Hold your horses.":" 耐心点儿。",
         
        "How can I get in touch with you?":" 我怎样能跟你联络上? ",

        "How do I look?":" 我看上去怎么样?",
         
        "How is it going?":" 情况怎么样?",
         
        "How late are you open?":" 你们营业到几点?",
         
        "How long did it last?":" 持续了多久?",
         
        "How long will it take to get there?":" 到那儿要多长时间? ",

        "How much is it?":" 多少钱?",
         
        "How often do you eat out?":" 你隔多久在外面吃一次饭?",
         
        "I apologize.":" 我很抱歉。",
         
        "I appreciate your invitation.":" 感谢你的邀请。",
         
        "I bet you can.":" 我确信你能做到。",
         
        "I can manage it by myself.":" 我自己可以应付。",
         
        "I can't afford it.":" 我买不起。",
         
        "I can't believe it.":" 我简直不敢相信。",
         
        "I can't resist the temptation.":" 我不能抵挡诱惑。",
         
        "I can't stand it.":" 我受不了。",
         
        "I can't tell.":" 我说不准。",
         
        "I couldn't agree more.":" 我完全同意。",
         
        "I couldn't get through.":" 我打不通电话。",
         
        "I couldn't help it.":" 我没有办法。",
         
        "I didn't mean to.":" 我不是故意的。",
         
        "I don't know for sure.":" 我不确定。",
         
        "I enjoy your company.":" 我喜欢有你做伴。",
         
        "I like it very much.":" 我非常喜欢。",
         
        "I envy you.":" 我羡慕你。",
         
        "I feel like having some cookies.":" 我很想吃饼干。",
         
        "I'm so sorry.":" 太对不起了。",
         
        "I feel the same way.":" 我也有同感。",
         
        "I have a complaint.":" 我要投诉。",
         
        "I have nothing to do with it.":" 那与我无关。",
         
        "I haven't the slightest idea.":" 我一点儿都不知道。",
         
        "I hope you'll forgive me.":" 我希望你能原谅我。"

        }


dict3 = {
        
        "I know the feeling.":" 我知道那种感觉。",
         
        "I mean what I say.":" 我说话算数。",
         
        "I owe you one.":" 我欠你一个人情。",
         
        "I really regret it.":" 我真的非常后悔。",
         
        "I think so.":" 我想是这样。",
         
        "I think so, too.":" 我也这样以为。",
         
        "I understand completely.":" 我完全明白。",
         
        "I want to report a theft.":" 我要报一宗盗窃案。",
         
        "I was just going to call you.":" 我正准备打电话给你。",
         
        "I was moved.":" 我很受感动。",
         
        "I wasn't aware of that.":" 我没有意识到。",
         
        "I wasn't born yesterday.":" 我又不是三岁小孩。",
         
        "I wish I could.":" 但愿我能。",
         
        "I wouldn't worry about it, if I were you.":" 如果我是你,我就不会担心。",

        "I'd like a refund.":" 我想要退款。",
         
        "I'd like to deposit some money.":" 我想存点儿钱。",
         
        "I'd like to make a reservation.":" 我想订票/房间。",
         
        "I'll be right with you.":" 我马上就来。",
         
        "I'll check it.":" 我去查一下。",
         
        "I'll do my best.":" 我将会尽我最大努力。",
         
        "I'll give you a hand.":" 我来帮助你。",
         
        "I'll have to think about that.":" 这事儿我得想一想再定。",

        "I'll keep my eyes open.":" 我会留意的。",
         
        "I'll keep that in mind.":" 我会记住的。",
         
        "I'll pay the bill.":" 我来付帐。",
         
        "I'll play it by ear.":" 我将见机行事。",
         
        "I'll see what I can do.":" 我看一看能怎么办。",
         
        "I'll show you.":" 我指给你看。",
         
        "I'll take care of it.":" 我来办这件事。",
         
        "I'll take it.":" 我要了。",
         
        "I'll take your advice.":" 我接受你的忠告。",
         
        "I'll think it over.":" 我仔细考虑一下。",
         
        "I'll treat you to diner.":" 我想请你吃晚饭。",
         
        "I'll walk you to the door.":" 我送你到门口。",
         
        "I'm broke.":" 我身无分文。",
         
        "I'm crazy about English.":" 我非常喜欢英语。",
         
        "I'm easy to please.":" 我很随和。",
         
        "I'm glad to hear that.":" 听到这消息我很高兴。",
         
        "I'm glad you enjoyed it.":" 你喜欢我就高兴。",
         
        "I'm good at it.":" 我做这个很在行。",
         
        "I'm in a good mood.":" 我现在心情很好。",
         
        "I'm in good shape.":" 我的身体状况很好。",
         
        "I'm just having a look.":" 我只是随便看看。",
         
        "I'm looking for a part-time job.":" 我正在找兼职工作。",
         
        "I'm looking forward to it.":" 我盼望着这件事。",
         
        "I'm lost.":" 我给搞糊涂了。",
         
        "I'm not feeling well.":" 我感觉不舒服。",
         
        "I'm not myself today.":" 我今天心神不宁。"
        
        
        }

dict4={
        "I'm on a diet.":" 我正在节食。",
         
        "I'm on my way.":" 我这就上路。",
         
        "I'm in a hurry.":" 我赶时间。",
         
        "I'm sorry I'm late.":" 对不起,我迟到了。",
         
        "I'm sorry to hear that.":" 听到这个消息我感到遗憾。",

        "I'm under a lot of pressure.":" 我的压力很大。",
         
        "I'm working on it.":" 我正在努力。",
        
        "I still have a cold.":" 我还是有点感冒。",
        
        "I've changed my mind.":" 我已经改变主意。",
         
        "I've got a headache.":" 我头痛。",
         
        "I've got my hands full.":" 我手头正忙。",
         
        "I'll tell you a good news.":" 我要告诉你一个好消息。",

        "I've got no idea.":" 我不知道。",
         
        "I've had enough.":" 我已经吃饱了。",
         
        "If I were in your shoes.":" 如果我站在你的立场上。",
         
        "Is that OK?":" 这样可以吗?",
         
        "Is this seat taken?":" 这位子有人坐吗?",
         
        "You are welcome.":" 不必客气。",
         
        "It can happen to anyone.":" 这事可能发生在任何人身上。",

        "It doesn't make any difference.":" 都一样。",
         
        "It doesn't matter to me.":" 这对我来说无所谓。",
         
        "It doesn't work.":" 它出故障了。",
         
        "It drives me crazy.":" 它使我快要发疯了。",
         
        "It isn't much.":" 这是微不足道的。",
         
        "It really comes in handy.":" 有了它真是方便。",
         
        "It slipped my mind.":" 我不留神忘了。",
         
        "It takes time.":" 这需要时间。",
         
        "It will come to me.":" 我会想起来的。",
         
        "It will do you good.":" 这会对你有好处。",
         
        "It won't happen again.":" 下不为例。",
         
        "It won't take much time.":" 不会花很多时间。",
         
        "It won't work.":" 行不通。",
         
        "It's nice meeting you.":" 很高兴认识你。",
         
        "It's a deal.":" 一言为定。",
         
        "It's a long story.":" 真是一言难尽。",
         
        "It's a nice day today.":" 今天天气很好。",
         
        "It's a once in a lifetime chance.":" 这是一生难得的机会。",
         
        "It's a pain in the neck.":" 这真是苦不堪言。",
         
        "It's a piece of cake.":" 这很容易。",
         
        "It's a small world.":" 这世界真小。",
         
        "It's a waste of time.":" 这是浪费时间。",
         
        "It's about time.":" 时间差不多了、是时候了。",
         
        "It's all my fault.":" 都是我的错。",
         
        "It's great.":" 棒极了!",

        "It's awful.":" 真糟糕。",
         
        "It's been a long time.":" 好久不见了。",
         
        "It's better than nothing.":" 总比没有好。",
         
        "It's essential.":" 这是必要的。",
         
        "It's hard to say.":" 很难说。",
         
        "It's incredible.":" 令人难以置信、不可思议。",
         
        "It's just what I want.":" 这正是我想要的。"
         
}
dict5 = {

        "It's my pleasure.":" 这是我的荣幸。",
         
        "It's no big deal.":" 这没什么大不了的。",
         
        "It's not your fault.":" 不是你的错。",
         
        "It's nothing.":" 小事情、不足挂齿。",
         
        "It's only a matter of time.":" 这只是时间问题。",
         
        "That's impossible.":" 这是不可能的。",
         
        "It's time for dinner.":" 该吃晚饭了。",
         
        "It's up in the air.":" 尚未决定。",
         
        "It's up to date.":" 这个很时兴。",
         
        "It's up to you.":" 一切由你决定。",
         
        "It's very popular.":" 它很受欢迎。",
         
        "It's worth seeing.":" 它绝对值得一看。",
        
        "Let it be.":"顺其自然。",
         
        "For safety's sake.":"为安全起见。",
         
        "Keep the change.":"不用找了。",
         
        "Keep up the good work.":"再接再厉。",
         
        "Keep your fingers crossed.":"为成功祈祷吧。",
         
        "Kill two birds with one stone.":"一举两得。",
         
        "I'll call you later.":"我过一会儿打给你吧。",
         
        "Let me guess.":"让我猜一猜。",
         
        "Let me put it this way.":"让我这么说吧。",
         
        "Let me see.":"让我想一想。",
         
        "Let's call it a day.":"我们今天就到这儿吧。",
         
        "Let's celebrate!":"让我们好好庆祝一下吧! ",

        "Let's find out.":"让我们找出(..真相)。",
         
        "Let's get to the point.":"让我们言归正传。",
         
        "Let's get together sometime.":"有时间我们聚一下吧。",
         
        "Let's hope for the best.":"让我们往好处想吧。",
         
        "Let's keep in touch.":"让我们保持联系。",
         
        "Let's make up.":"让我们言归于好吧。",
         
        "Let's go visit them.":"让我们去拜访他们吧。",
         
        "We can talk while we eat.":"我们可以边吃边谈。",
         
        "Long time no see.":"好久不见。",
         
        "Look before you leap.":"三思而后行。",

        "May I ask you a question?":"我可以问一个问题吗?",
         
        "May I have a receipt?":"我可以要一张收据吗?",
         
        "May I have your name?":"请问你叫什么名字?",
         
        "May I pay by credit card?":" 我可以用信用卡付款吗?",
         
        "May I try it on?":" 我能试穿一下吗?",
         
        "Maybe it will work.":" 也许这个办法会有效。",
         
        "Maybe another time.":" 也许下一次吧。",
         
        "My mouth is watering.":" 我在流口水了。",
         
        "My phone was out of order.":" 我的电话坏了。",
         
        "No pain, no gain.":" 不劳则无获。",
         
        "No problem.":" 没问题。",
         
        "Nothing is impossible to a willing heart.":" 心之所愿,无事不成。",
         
        "Pain past is pleasure.":" 过去的痛苦即是快乐。",
         
        "Please accept my apology.":" 请接受我的道歉。",
         
        "Please don't blame yourself.":" 请不要责怪你自己。",

        "Please leave me alone.":" 请别打扰我。"
    }

dict6 = {
        "Please let me know.":" 请告诉我一声。",
         
        "Please make yourself at home.":" 请别客气。",
         
        "Please show me the menu.":" 请把菜单给我。",

        "Probably.":" 可能吧。",
         
        "So far, so good.":" 到目前为止还好。",

        "Something must be done about it.":" 必须得想个办法。",

        "I think something's happened to us.":" 我想我们之间发生了一些事。",
         
        "Storms make trees take deeper roots.":" 风暴使树木深深扎根。",

        "Suit yourself.":" 随你的便。",
         
        "Take care.":" 请多保重。",
         
        "Take it or leave it.":" 要不要由你。",
         
        "Take my word for it.":" 相信我的话。",
         
        "Take your time.":" 慢慢来。",
         
        "Thank you all the same.":" 不管怎样还是要谢谢你。",

        "Thank you for everything.":" 感谢你做的一切。",

        "Thanks a million.":" 非常感谢。",
         
        "Thanks for the warning.":" 谢谢你的提醒。",
         
        "Thanks for your cooperation.":" 多谢合作。",
         
        "That couldn't be better.":" 那再好不过了。",
         
        "That depends.":" 看情况。",
         
        "That makes sense.":" 那可以理解。",
         
        "That reminds me.":" 那可提醒我了。",
         
        "That rings a bell.":" 听起来耳熟。",
         
        "That sounds like a good idea.":" 那听上去是个好主意。",

        "That's all right.":" 没关系。",
         
        "That's disgusting.":" 真讨厌。",
         
        "That's fair.":" 那样公平。",
         
        "That's for sure.":" 那是肯定的。",
         
        "That's good to know.":" 幸好知道了这件事。",
         
        "That's just what I was thinking.":" 我也是这么想的。",
         
        "That's life.":" 这就是生活。",
         
        "That's more like it.":"这还差不多。",
         
        "That's not a problem.":"那不是问题。",
         
        "That's not true.":" 那不是真的!",
         
        "That's OK.":" 可以。",
         
        "That's ridiculous.":" 那太荒唐了。",
         
        "That's what I think.":" 我就是这么想的。",
         
        "That's the way it is.":" 就是这样。",
         
        "That's worthwhile.":" 那是值得的。",
         
        "The same to you.":" 你也一样。",
         
        "The shortest answer is doing.":" 最简短的回答是干。",
         
        "The sooner, the better.":" 愈快愈好。",
         
        "There is a call for you.":" 有你的电话。",
         
        "There is no doubt about it.":" 那是毫无疑问的。",
         
        "There is nothing I can do.":" 我无能为力。",
         
        "There's a possibility.":" 有这个可能。",
         
        "These things happen all the time.":" 这是常有的事。",
         
        "This soup tastes great.":" 这个汤非常美味。",
         
        "Time is money.":" 时间就是金钱。",
         
        "Tomorrow never comes.":" 莫依赖明天。"

    }
dict7 = {

        "Two heads are better than one.":" 人多智广。",
         
        "We are in the same boat.":" 我们的处境相同。",
         
        "We can get by.":" 我们过得去。",
         
        "We can work it out.":" 我们可以解决这个问题。",
         
        "We have a lot in common.":" 我们有很多相同之处。",
         
        "Let's talk another day":" 改天再说吧。",
         
        "What a coincidence!":" 真是太巧了!",
         
        "What a pity!":" 真是遗憾!",
         
        "What are you up to?":" 你想做什么?",
         
        "What are you talking about?":" 你在说什么?",
         
        "What are your plans for the weekend?":" 你周末计划做什么? ",

        "What can I do for you?":" 要我帮忙吗?",
         
        "What do you do for relaxation?":" 你做什么消遣。",
         
        "What do you recommend?":" 你推荐什么?",
         
        "What do you think of my new car?":" 你觉得我的新车怎么样? ",

        "What do you think?":" 你觉得怎么样?",
         
        "What is it about?":" 这是关于什么的。",
         
        "What is it like there?":" 那儿怎么样?",
    
        "Why do you say that?":" 你怎么这么说呢?",
         
        "What's going on?":" 发生了什么事了?",
         
        "What are you thinking about?":" 你在想什么呢?",
         
        "What's the deadline?":" 截止到什么时候?",
         
        "What's the matter with you?":" 你怎么啦?",
         
        "What's the purpose of your visit?":" 你来访的目的是什么? ",

        "What's the weather like?":" 天气怎么样?",
         
        "What's your favorite food?":" 你最喜欢的食物是什么? ",

        "What's your job?":" 你做什么工作?",
         
        "Whatever you think is fine with me.":" 我随你。",
         
        "When is the most convenient time for you?":" 你什么时候最方便? ",

        "When will it be ready?":" 什么时候能准备好?",
         
        "Where are you going?":" 你去哪儿?",
         
        "Where can I check in?":" 在哪儿办理登记手续? ",

        "How should I do?":" 我该怎么办呢?",
         
        "Where do you live?":" 你住在哪儿?",
         
        "Where have you been?":" 你去哪儿了?",
         
        "Where is the rest room, please?":" 请问洗手间在哪儿? ",

        "Where were we?":" 我们说到哪儿了?",
         
        "Who is in charge here?":" 这里谁负责?",
         
        "Would you like a drink?":" 你要不要来点儿喝的? ",

        "Would you do me a favor?":" 你能帮我一个忙吗?",
         
        "You are just saying that.":" 你只是说说而已。",
         
        "You are kidding.":" 你开玩笑吧。",
         
        "You are so considerate.":" 你真有心。",
         
        "You can count on me.":" 你可以指望我。",
         
        "I agree.":" 我同意。",
         
        "You can't complain.":" 你该知足了。",
         
        "You deserve it.":" 这是你应得的。",
         
        "You did a good job.":" 你干得很好。",
         
        "You get what you pay for.":" 一分钱一分货。",
         
        "You got a good deal.":" 你买得真便宜。"
    }

dict8 = {
        "You need a holiday.":" 你需要休假。",
         
        "You never know.":" 世事难料。",
         
        "You said it.":" 你算说对了。",
         
        "You should try it.":" 你应该试一试。",
         
        "You should take advantage of it.":" 你应该好好利用它。",

        "You will be better off.":" 你的处境将更好。",
         
        "You will have to wait and see.":" 你得等一等看。",
         
        "You'll get used to it.":" 你会习惯的。",
         
        "You've dialed the wrong number.":" 你拨错电话号码了。",
         
        "You have a point.":" 你说的有道理。",
         
        "You've got it.":" 你明白了。",
         
        "You've made a good choice.":" 你的眼力不错。",
         
        "Your satisfaction is guaranteed.":" 包你满意。",

        "I'll be right back.":"我马上回来",

        "How have you been?":"你最近怎么样？",

        "That's what I've heard":"我也听说了",

        "What's the date today?":"今天几号?",

        "Five minutes or so.":"5分钟左右。",

        "I'm leaving on Sunday.":"我周日走",#诸如leave,arrive,go,come等表空间趋向性动词用现在进行时态表示将来#

        "When are you coming back?":"你什么时候回来？",#诸如leave,arrive,go,come等表空间趋向性动词用现在进行时态表示将来#

        "They are missing in action.":"他们缺乏行动。",

        "Forgive me for my being rude that day.":"请原谅我那天的无礼。",

        "I heard the boss of the bar was arrested.":"我听说那间酒吧的老板被逮捕了。",

        "You'd better send him to the hospital now.":"你最好现在就把他送到医院。",

        "In my opinion, you did the right thing.":"在我看来，你做的是对的。",

        "As far as I'm concerned, he is the best teacher in the school.":"就我而言，他是学校里最好的老师。",

        
    }
dict9 = {

    }
dict10 = {

    }

dictWrong = {};



def testDict(dic):
    print("Start!")
    count = len(dic)
    i = 0
    yes=0
    for v, k in dic.items():
        i+=1;
        print ("%d/%d %s (type 'a' to see the answer)" % (i,count,k))
        while 1:
            str = input();
            if str == 'a':
                print (v)
                xx = {v:k}
                dictWrong.update(xx)
                break
            if str in v and len(str) == len(v)-1:
                yes+=1
                if i==count:
                    break
                print ("Right!~")
                break
            else:
                print ("Wrong!~ Pls check!")
    print("The testing is over,and your score is %d/%d" % (yes,count))
    print ("Error____________________________________")
    print (dictWrong)

def testDictWithKeys(dic,keys):
    print("Start!")
    count = len(keys)
    i = 0
    yes=0
    for v, k in dic.items():
        if v in keys:
            i+=1;
            print ("%d/%d %s (type 'a' to see the answer)" % (i,count,k))
            while 1:
                str = input();
                if str == 'a':
                    print (v)
                    xx = {v:k}
                    dictWrong.update(xx)
                    break
                if str in v and len(str) == len(v)-1:
                    yes+=1
                    if i==count:
                        break
                    print ("Right!~")
                    break
                else:
                    print ("Wrong!~ Pls check!")
    print("The testing is over,and your score is %d/%d" % (yes,count))
    print ("Error____________________________________")
    print (dictWrong)

print("Welcome to SentenceTesting! Type '1-10' to do group testing,or input a number more than 10 to do random testing.")
cmd = input();
if cmd=='1':
    testDict(dict1)
elif cmd == '2':
    testDict(dict2)
elif cmd == '3':
    testDict(dict3)
elif cmd == '4':
    testDict(dict4)
elif cmd == '5':
    testDict(dict5)
elif cmd == '6':
    testDict(dict6)
elif cmd == '7':
    testDict(dict7)
elif cmd == '8':
    testDict(dict8)
elif cmd == '9':
    testDict(dict9)
elif cmd == '10':
    testDict(dict10)    
elif cmd > '10':
    dictMix = {**dict3, **dict6, **dict2, **dict4, **dict1, **dict7, **dict8, **dict5}
    keys = random.sample(dictMix.keys(), int(cmd))  # 随机一个字典中的key，第二个参数为限制个数
    testDictWithKeys(dictMix,keys)
