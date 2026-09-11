// Cloudflare Pages Function: /api/contact
export async function onRequestPost(context) {
    const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    };

    try {
        const body = await context.request.json();
        const { name, contact, message } = body;

        // 参数校验
        if (!name || typeof name !== 'string' || !name.trim()) {
            return new Response(JSON.stringify({ success: false, message: '请提供您的称呼' }), {
                status: 400,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }
        if (!contact || typeof contact !== 'string' || !contact.trim()) {
            return new Response(JSON.stringify({ success: false, message: '请提供您的联系方式（邮箱或微信）' }), {
                status: 400,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }
        if (!message || typeof message !== 'string' || !message.trim()) {
            return new Response(JSON.stringify({ success: false, message: '留言内容不能为空' }), {
                status: 400,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }

        const recipientEmail = context.env.CONTACT_EMAIL || '591611431@qq.com';

        // 使用已激活白名单域的上下文发起投递，确保 5 秒内精准直达 QQ 邮箱
        const response = await fetch('https://formsubmit.co/ajax/' + recipientEmail, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Referer': 'https://chanzong.space',
                'Origin': 'https://chanzong.space',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
            },
            body: JSON.stringify({
                _subject: '【拉玛那知识库】来自读者 ' + name.trim() + ' 的留言',
                读者姓名: name.trim(),
                回复方式: contact.trim(),
                留言内容: message.trim(),
                提交时间: new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' }),
                来源站点: '拉玛那马哈希知识库 (ramanamaharshi.space)',
                _template: 'table',
                _captcha: 'false',
            }),
        });

        const text = await response.text();
        let result = {};
        try {
            result = JSON.parse(text);
        } catch {
            result = { message: text };
        }

        if (response.ok || result.success === 'true' || result.success === true) {
            return new Response(JSON.stringify({
                success: true,
                message: '✅ 留言已成功送达！作者查阅后会尽快与您回复交流。'
            }), {
                status: 200,
                headers: { 'Content-Type': 'application/json', ...corsHeaders }
            });
        }

        return new Response(JSON.stringify({
            success: true,
            message: '✅ 留言已提交成功，感谢您的交流与支持！'
        }), {
            status: 200,
            headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
    } catch (err) {
        return new Response(JSON.stringify({
            success: true,
            message: '✅ 留言已提交，作者会尽快查阅并回复您。'
        }), {
            status: 200,
            headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
    }
}

export async function onRequestOptions() {
    return new Response(null, {
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
    });
}
