$(document).ready(function(){
    var team = {
        hannah: {
            name:'Hannah Oh',
            bio: 'Hannah Oh is a student at Bellevue High School. She spent descent amount of her childhood in South Korea; however, she is currently living in Bellevue, WA. She started working for Harvix in 2013, in the Marketing and Business development. When Hannah has free time, she mostly spends her time on Cross Country running. Currently, she is involved in Robotics club and Seattle Girls Choir. In the future, Hannah hopes to go into IT business field. If you need to contact Hannah, feel free to contact her at: hannahoh0102@gmail.com',
            role: 'Executive Business Development Associate'
        },
        sarthak: {
            name: 'Sarthak Srivastava',
            bio: 'Sarthak Srivastava is a 13 years old boy from Allahabad, India.He studies in 8th grade in Bishoip Johnson School and College.He is aspiring programmer in PHP, Python and currently doing development in Java.I am interested in making android apps and I am currently making a game in Android.i love working in Harvix as everyone here is of my age-group and Rich Skrenta is one of my ideals who helped me lot in the road of programming.I want to establish a MultiNational firm of my own and work in Harvix at my best',
            role: 'Software engineer'
        },
        minh: {
            name: 'Minh Le',
            bio: 'Minh is a student in Perth. He is dedicated to web design and user experience and have started working for Harvix in 2013 as a UI designer. His job is to enhance user experience at Harvix. If you don\'t find him in front of his computer, he would be playing sport or hanging out with friends. Minh hopes to enter computer science field. Contact him at: vietminhle98@gmail.com',
            role: 'UI designer'
        },
        armando: {
            name:'Armando Ortiz',
            bio: 'Armando Ortiz is a student at Bellevue High School. He was raised in Seattle, WA; and now he currently lives in Bellevue, WA. He had the privilege to join Harvix in 2013, in the Marketing department. He has been involved in helping the community while he was on the Exec. Committee of the National Junior Honors Society and currently in Key Club. During his free time Armando enjoys spending time with his family, playing soccer, running, and making digital projects. In the future he Armando hopes to go into the Digital/Computer Engineering field. If you need to Contact Armando you can reach him at: armando.ortiz10@live.com',
            role: 'VP Marketing'
        },
        jakob: {
            name: 'Jakob Piccitto',
            bio: 'Jakob is a 15-year-old student who experienced most of his childhood in Menlo Park, California, and currently lives in Bellevue, Washington with his family. Jakob began work on Harvix in 2013 after he was recruited by a former employee who had been his friend in California. Since then, Jakob has had the privilege to oversee the marketing and business development of Harvix, and is working extensively on the implementation of Harvix in schools. When not working on Harvix, he enjoys running cross-country and playing the saxophone. In the future, Jakob hopes to receive achieve an MBA and establish himself in the corporate world. For inquiries regarding partnerships, investments, donations, and more, Jakob can be contacted at jhpicciotto@gmail.com.',
            role: 'VP Bussiness Developement'
        },
        anh: {
            name: 'Anh Viet Le',
            bio: 'Anh is a young student in Australia. He is known for his love with programming and working effectively in a short amount of time. When he encounter any bugs, he would research it everywhere possible, or occasionally smashes his computer into pieces. He believes that â€˜What makes a website a website is the interaction. Without it we would just draw the website insteadâ€™. In his free time, this geek usually play indie games or make a simple game without any graphics whatsoever. Contact him at: anhlevietexe@gmail.com',
            role: 'Front-end engineer'
        },
        ivan: {
            name: 'Ivan Zdane',
            bio: 'Ivan is a 13 year old and a student in Toronto, Canada. Ivan began working at Harvix in 2013 as a software developer. In his free time, he enjoys taking online courses, cross-country and playing his cello. In the future, Ivan hopes to go into the computer science/engineering field. You can reach Ivan at: izdane@gmail.com',
            role: 'IOS developer'
        },
        nishi: {
            name: 'Nishi Jain',
            bio: '',
            role: 'Executive Business Development Associate'
        },
        julie: {
            name:'Julie White',
            bio: '',
            role: 'Public Relations Director'
        },
        david: {
            name:'David Skrenta',
            bio: '',
            role: 'CEO, Founder'
        },
        bryce: {
            name: 'Bryce DesBrisay',
            bio: '',
            role: 'CCO, Founder'
        },
        avi: {
            name: 'Avi Bajpai',
            bio: '',
            role: 'Marketing and Finance Director'
        },
	shant: {
            name: 'Shant Narkizian',
            bio: '',
            role: 'Executive Business Development Associate'
        }
        
    }
    $('#team ul li').click(function(e) {
        var nameTrig = e.target.getAttribute('id');
        $('#teamoverlay').css({
            'z-index':'999',
            'opacity':'1',
            'height':'300px'
        });
        $('#teamoverlay img').attr('src','http://harvix.com/about/images/' +nameTrig + '.jpg');
        $('#teamoverlay h3').html(team[nameTrig].name + ' - ' + team[nameTrig].role);
        $('#teamoverlay p').html(team[nameTrig].bio);
        $('#team').css('height', '300px');
        $('#contact').css('margin-top', '3040px');
        $('footer').css('margin-top', '3340px');
        $('#team').css('opacity', 0);
    });
    $('#close').click(function() {
        $('#teamoverlay').css({
            'z-index':'30',
            'opacity':'0',
            'height':'500px'
        });
        $('#team').css('height', '500px');
        $('#contact').css('margin-top', '3240px');
        $('footer').css('margin-top', '3540px');
        $('#team').css('opacity', 1);
    });
}); 
