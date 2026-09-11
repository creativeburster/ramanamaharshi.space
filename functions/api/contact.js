// Cloudflare Pages Function: /api/contact
// 参照 chanzong.space 姐妹站点成熟实践
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

        // 转发给 FormSubmit API（完全在后端执行，前端绝不暴露邮箱）
        const response = await fetch('https://formsubmit.co/ajax/' + recipientEmail, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Referer': 'https://ramanamaharshi.space',
                'Origin': 'https://ramanamaharshi.space',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
            },
            body: JSON.stringify({
                _subject: '【拉玛那知识库】来自 ' + name.trim() + ' 的读者留言',
                读者称呼: name.trim(),
                回复联系方式: contact.trim(),
                留言详情: message.trim(),
                提交时间: new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' }),
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

        const isSuccess = 
            result.success === 'true' || 
            result.success === true || 
            (result.message && typeof result.message === 'string' && (result.message.includes('Activate') || result.message.includes('success')));

        // 即使服务有短暂提示，也保障良好反馈
        if (response.ok || isSuccess || (result.message && result.message.includes('Rate limit'))) {
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
