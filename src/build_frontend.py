import base64, os

with open('/mnt/user-data/uploads/WhatsApp_Image_2026-05-14_at_12_18_13.jpeg','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

with open('/home/claude/safety-first/src/frontend_css.css','r') as f:
    CSS = f.read()

LN  = '<img src="data:image/jpeg;base64,' + LOGO + '" class="tke-logo-img" alt="TKE">'
LA  = '<img src="data:image/jpeg;base64,' + LOGO + '" alt="TKE" style="height:44px;width:auto;border-radius:6px;padding:4px 7px;background:white;">'
LF  = '<img src="data:image/jpeg;base64,' + LOGO + '" alt="TKE" style="height:28px;width:auto;border-radius:4px;padding:2px 5px;background:white;">'
LRU = '<img src="data:image/jpeg;base64,' + LOGO + '" alt="TKE" style="height:36px;width:auto;border-radius:4px;padding:2px 6px;background:white;">'

with open('/home/claude/safety-first/src/app.js','r') as f:
    JS = f.read()

HTML = (
'<!DOCTYPE html>\n'
'<html lang="fr" data-theme="light">\n'
'<head>\n'
'<meta charset="UTF-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
'<title>Safety First - TK Home Solutions</title>\n'
'<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900'
'&family=Barlow+Condensed:wght@700;800;900&family=Nunito:wght@400;600;700;800;900'
'&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">\n'
'<style>\n' + CSS + '\n</style>\n'
'</head>\n<body>\n\n'

'<div class="api-loading" id="api-loading" style="display:none;">'
'<div class="api-loading-box"><div class="spinner"></div>'
'<p id="api-loading-text">Chargement...</p></div></div>\n'
'<div id="toast"></div>\n\n'

# ═══════════ LANDING ═══════════
'<div id="landing" class="view active">\n'
'<nav>\n' + LN + '\n'
'<div class="nav-right">\n'
'<button class="lang-btn" id="lang-btn" onclick="switchLang()">EN</button>\n'
'<div class="nav-divider"></div>\n'
'<div class="theme-toggle" onclick="toggleTheme()">'
'<span class="toggle-emoji" id="toggle-emoji">sun</span>'
'<div class="toggle-track"></div>'
'<span class="theme-toggle-label" id="toggle-label">Mode clair</span></div>\n'
'<button class="btn-ghost" onclick="gotoLogin()">Se connecter</button>\n'
'<button class="btn-primary" onclick="gotoRegister()">Cr&#233;er un compte</button>\n'
'</div></nav>\n'
'<section class="hero">\n'
'<div class="hero-badge">Plateforme interne TK Home Solutions</div>\n'
'<h1 class="hero-title">La s&#233;curit&#233;<br><span class="gradient-text">Avant tout.</span></h1>\n'
'<p class="hero-sub">Un hub centralis&#233; de s&#233;curit&#233; au travail pour les employ&#233;s de TK Home Solutions &#8212; suivez les indicateurs en temps r&#233;el, restez inform&#233;s des campagnes, participez aux quiz et signalez les conditions dangereuses, tout en un seul endroit.</p>\n'
'<div class="hero-ctas">'
'<button class="btn-large primary" onclick="gotoLogin()">Se connecter</button>'
'<button class="btn-large ghost" onclick="gotoRegister()">Cr&#233;er un compte</button>'
'</div>\n</section>\n'
'<section class="features">\n'
'<div class="section-label">Ce que nous offrons</div>\n'
'<h2 class="section-title">Tout pour la s&#233;curit&#233;,<br>con&#231;u pour votre &#233;quipe</h2>\n'
'<div class="features-grid">'
'<div class="feature-card"><div class="feature-icon icon-purple">&#128202;</div><h3>Tableau de bord en direct</h3><p>Indicateurs cl&#233;s mis &#224; jour par les administrateurs.</p></div>'
'<div class="feature-card"><div class="feature-icon icon-orange">&#128226;</div><h3>Campagnes s&#233;curit&#233;</h3><p>Suivez les initiatives Stop The Shock, We Get Home et bien d\'autres.</p></div>'
'<div class="feature-card"><div class="feature-icon icon-teal">&#129504;</div><h3>Quiz s&#233;curit&#233; hebdomadaire</h3><p>Testez vos connaissances avec des quiz interactifs courts.</p></div>'
'<div class="feature-card"><div class="feature-icon icon-purple">&#9888;</div><h3>Signalement d\'incidents</h3><p>Signalez les conditions non s&#233;curis&#233;es instantan&#233;ment.</p></div>'
'<div class="feature-card"><div class="feature-icon icon-orange">&#128737;</div><h3>Guide EPI &amp; S&#233;curit&#233;</h3><p>10 r&#232;gles, 5 pi&#232;ges, guide PPE &#8212; toujours &#224; port&#233;e.</p></div>'
'<div class="feature-card"><div class="feature-icon icon-teal">&#9879;</div><h3>Produits chimiques</h3><p>Classifications de danger et instructions de manipulation.</p></div>'
'</div>\n</section>\n'
'<footer>' + LF + '<div class="copy">2026 TK Home Solutions &middot; Safety First &middot; Usage interne uniquement</div></footer>\n'
'</div>\n\n'

# ═══════════ LOGIN ═══════════
'<div id="login-page" class="view">\n'
'<div class="auth-page">\n'
'<div class="auth-left"><div class="auth-left-content">\n'
'<div class="auth-left-logo">' + LA + '</div>\n'
'<h2 id="ll-title">Bon retour<br>parmi nous.</h2>\n'
'<p id="ll-sub">Connectez-vous pour acc&#233;der &#224; votre tableau de bord TK Home Solutions.</p>\n'
'<div class="auth-features-list">'
'<div class="auth-feature-item"><span class="dot"></span><span id="ll-f1">Indicateurs de s&#233;curit&#233; en direct</span></div>'
'<div class="auth-feature-item"><span class="dot"></span><span id="ll-f2">Moments s&#233;curit&#233; hebdomadaires</span></div>'
'<div class="auth-feature-item"><span class="dot"></span><span id="ll-f3">Signalement d\'incidents</span></div>'
'<div class="auth-feature-item"><span class="dot"></span><span id="ll-f4">Notifications lors des mises &#224; jour</span></div>'
'</div>\n</div></div>\n'
'<div class="auth-right"><div class="auth-form-wrap">\n'
'<button class="auth-back" onclick="gotoLanding()">&larr; <span id="l-back">Retour &#224; l\'accueil</span></button>\n'
'<div class="auth-form-title" id="l-title">Connexion</div>\n'
'<div class="auth-form-sub" id="l-sub">Utilisez votre compte entreprise TK Home Solutions</div>\n'
'<div class="alert-box err" id="login-err"></div>\n'
'<div class="form-group"><label id="l-el">Email professionnel</label>'
'<input type="email" id="login-email" placeholder="prenom.nom@tkelevator.com" />'
'<div class="field-hint info" id="l-eh">Doit &#234;tre une adresse @tkelevator.com</div></div>\n'
'<div class="form-group"><label id="l-pl">Mot de passe</label>'
'<input type="password" id="login-pass" placeholder="Entrez votre mot de passe" onkeydown="if(event.key===\'Enter\')doLogin()" /></div>\n'
'<button class="form-submit" id="l-btn" onclick="doLogin()">Se connecter</button>\n'
'<div class="auth-switch"><span id="l-sw">Pas encore de compte&#160;? </span><a id="l-swl" onclick="gotoRegister()">Cr&#233;er un compte</a></div>\n'
'</div></div></div></div>\n\n'

# ═══════════ REGISTER ═══════════
'<div id="register-page" class="view">\n'
'<div class="auth-page">\n'
'<div class="auth-left"><div class="auth-left-content">\n'
'<div class="auth-left-logo">' + LA + '</div>\n'
'<h2 id="rl-title">Rejoignez le<br>Hub S&#233;curit&#233;.</h2>\n'
'<p id="rl-sub">Cr&#233;ez votre compte pour acc&#233;der &#224; la plateforme Safety First de TK Home Solutions.</p>\n'
'<div class="auth-features-list">'
'<div class="auth-feature-item"><span class="dot"></span><span id="rl-f1">R&#233;serv&#233; aux @tkelevator.com</span></div>'
'<div class="auth-feature-item"><span class="dot"></span><span id="rl-f2">V&#233;rification par email obligatoire</span></div>'
'<div class="auth-feature-item"><span class="dot"></span><span id="rl-f3">Acc&#232;s s&#233;curis&#233; aux employ&#233;s</span></div>'
'<div class="auth-feature-item"><span class="dot"></span><span id="rl-f4">Acc&#232;s imm&#233;diat au tableau de bord</span></div>'
'</div>\n</div></div>\n'
'<div class="auth-right"><div class="auth-form-wrap">\n'
'<button class="auth-back" onclick="gotoLanding()">&larr; <span id="r-back">Retour &#224; l\'accueil</span></button>\n'
'<div id="reg-form-step">\n'
'<div class="auth-form-title" id="r-title">Cr&#233;er un compte</div>\n'
'<div class="auth-form-sub" id="r-sub">R&#233;serv&#233; aux employ&#233;s TK Home Solutions</div>\n'
'<div class="alert-box err" id="reg-err"></div>\n'
'<div class="form-group"><label id="r-nl">Nom complet</label><input type="text" id="reg-name" placeholder="Jean Dupont" /></div>\n'
'<div class="form-group"><label id="r-el">Email professionnel</label>'
'<input type="email" id="reg-email" placeholder="prenom.nom@tkelevator.com" oninput="validateEmailField()" />'
'<div class="field-hint info" id="email-hint">Doit se terminer par @tkelevator.com</div></div>\n'
'<div class="form-group"><label id="r-idl">Matricule employ&#233; (facultatif)</label><input type="text" id="reg-empid" placeholder="ex. TKE-00421" /></div>\n'
'<div class="form-group"><label id="r-pl">Mot de passe</label>'
'<input type="password" id="reg-pass" placeholder="8 caract&#232;res minimum" oninput="validatePass()" />'
'<div class="field-hint info" id="pass-hint">Au moins 8 caract&#232;res</div></div>\n'
'<div class="form-group"><label id="r-p2l">Confirmer le mot de passe</label>'
'<input type="password" id="reg-pass2" placeholder="R&#233;p&#233;tez votre mot de passe" oninput="validatePass2()" />'
'<div class="field-hint" id="pass2-hint" style="display:none"></div></div>\n'
'<button class="form-submit" id="reg-submit-btn" onclick="doRegister()">Cr&#233;er le compte &amp; v&#233;rifier l\'email</button>\n'
'<div class="auth-switch"><span id="r-sw">D&#233;j&#224; un compte&#160;? </span><a id="r-swl" onclick="gotoLogin()">Se connecter</a></div>\n'
'</div>\n'
'<div id="reg-verif-step" style="display:none">\n'
'<div class="auth-form-title">V&#233;rifiez votre email</div>\n'
'<div class="auth-form-sub">Un lien de v&#233;rification a &#233;t&#233; envoy&#233; &#224; votre adresse.</div>\n'
'<div class="verif-box" style="display:block"><div class="verif-icon">&#128231;</div>'
'<h4>Email de v&#233;rification envoy&#233;</h4>'
'<p>Nous avons envoy&#233; un lien &#224;<br><strong id="sent-email-display" style="color:#6b21a8"></strong><br><br>Cliquez sur le lien pour activer votre compte. V&#233;rifiez vos spams si n&#233;cessaire.</p>'
'<button class="resend-btn" onclick="resendEmail()">Renvoyer l\'email</button></div>\n'
'<div class="alert-box ok" id="resend-ok" style="margin-top:12px;display:none">Email renvoy&#233;&#160;!</div>\n'
'<button class="form-submit" style="margin-top:8px" onclick="gotoLogin()">Retour &#224; la connexion</button>\n'
'</div>\n'
'</div></div></div></div>\n\n'

# ═══════════ DASHBOARD ═══════════
'<div id="dashboard-page" class="view" style="background:#f1f4f7;min-height:100vh;">\n'
'<div style="width:100%;background:linear-gradient(135deg,#3b0a8a 0%,#6a35b5 45%,#f97316 100%);padding:32px 24px 24px;">'
'<div style="display:flex;justify-content:space-between;align-items:flex-start;max-width:700px;margin:0 auto;">'
'<div>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:28px;font-weight:900;color:white;">Safety First</div>'
'<div style="font-size:13px;color:rgba(255,255,255,.82);margin-top:4px;">TK Home Solutions</div>'
'<div id="dash-user-name" style="font-size:12px;color:rgba(255,255,255,.7);margin-top:2px;"></div>'
'</div>'
'<div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end;">'
'<button onclick="gotoAdminLogin()" style="background:rgba(255,255,255,.18);border:1.5px solid rgba(255,255,255,.3);color:white;border-radius:10px;padding:8px 14px;font-size:12px;font-weight:700;cursor:pointer;font-family:\'Nunito\',sans-serif;">&#9881; Admin</button>'
'<button onclick="doLogout()" style="background:rgba(239,68,68,.25);border:1.5px solid rgba(239,68,68,.4);color:white;border-radius:10px;padding:8px 14px;font-size:12px;font-weight:700;cursor:pointer;font-family:\'Nunito\',sans-serif;">&#x2715; D&#233;connexion</button>'
'</div></div></div>\n'
'<div id="last-updated-bar" style="text-align:center;font-size:11px;color:#9ca3af;padding:10px 0 0;"></div>\n'
'<div style="padding:16px 16px 40px;max-width:700px;margin:0 auto;">\n'

# Stats card
'<div class="dash-card">\n'
'<div class="dash-card-title">Tableau de bord s&#233;curit&#233;</div>\n'
'<div class="dash-stat-row">'
'<div class="dash-stat"><div class="dash-stat-num" style="color:#0fbcb0;" id="u-days">&#8212;</div><div class="dash-stat-lbl">Jours sans accident</div></div>'
'<div class="dash-divider"></div>'
'<div class="dash-stat"><div class="dash-stat-num" style="color:#f97316;" id="u-unsafe">&#8212;</div><div class="dash-stat-lbl">Conditions non s&#233;curis&#233;es</div></div>'
'<div class="dash-divider"></div>'
'<div class="dash-stat"><div class="dash-stat-num" style="color:#ef4444;" id="u-sif">&#8212;</div><div class="dash-stat-lbl">SIF</div></div>'
'</div></div>\n'

# Safety Moment card (dynamic)
'<div class="dash-card">\n'
'<div class="dash-card-title" id="u-moment-title">Moment S&#233;curit&#233;</div>\n'
'<div id="u-moment" style="font-size:14px;color:#374151;text-align:center;line-height:1.6;padding:8px 8px 16px;">Le message de s&#233;curit&#233; de la semaine appara&#238;tra ici.</div>\n'
'<button class="dash-btn-purple" id="u-moment-btn">Lire plus</button>\n'
'</div>\n'

# Campaigns card (dynamic)
'<div class="dash-card">\n'
'<div class="dash-card-title" id="u-camp-title">Campagnes S&#233;curit&#233;</div>\n'
'<div class="dash-card-sub" id="u-camp-sub">S&#233;lectionnez une campagne pour en savoir plus sur nos initiatives.</div>\n'
'<button class="dash-btn-purple" id="u-camp1-btn" onclick="gotoCampaigns()">Campagne 1</button>\n'
'<button class="dash-btn-orange" id="u-camp2-btn" onclick="gotoCampaigns()">Campagne 2</button>\n'
'</div>\n'

# Feature grid
'<div class="dash-grid">\n'
'<div class="dash-feat" onclick="gotoRules()">'
'<span style="font-size:28px;">&#128203;</span>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:13px;font-weight:800;color:#ec4899;margin-top:8px;" id="fg-rules">10 R&#232;gles s&#233;curit&#233;</div>'
'</div>'
'<div class="dash-feat" onclick="gotoTraps()">'
'<span style="font-size:28px;">&#9888;</span>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:13px;font-weight:800;color:#ef4444;margin-top:8px;" id="fg-traps">5 Pi&#232;ges</div>'
'</div>'
'<div class="dash-feat">'
'<span style="font-size:28px;">&#128737;</span>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:13px;font-weight:800;color:#ec4899;margin-top:8px;" id="fg-ppe">Guide EPI</div>'
'</div>'
'<div class="dash-feat" onclick="gotoReport()">'
'<span style="font-size:28px;">&#128680;</span>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:13px;font-weight:800;color:#f97316;margin-top:8px;" id="fg-report">Signaler un incident</div>'
'</div>'
'</div>\n'

# Quiz
'<div class="dash-card">'
'<div style="display:flex;align-items:center;">'
'<div style="flex:1;text-align:center;"><div style="font-size:28px;margin-bottom:6px;">&#129504;</div><div style="font-size:12px;color:#6b7280;font-weight:500;" id="fg-quiz-lbl">Quiz s&#233;curit&#233;</div></div>'
'<div style="width:1px;height:60px;background:#f0f0f0;"></div>'
'<div style="flex:1;text-align:center;"><div style="font-family:\'Nunito\',sans-serif;font-size:38px;font-weight:900;color:#0fbcb0;" id="u-quiz">&#8212;</div><div style="font-size:12px;color:#6b7280;margin-top:4px;" id="fg-score-lbl">Score quiz</div></div>'
'</div></div>\n'

# Chemical
'<div class="dash-card" style="text-align:center;cursor:pointer;">'
'<div style="font-size:36px;margin-bottom:8px;">&#9879;</div>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:14px;font-weight:800;color:#6a35b5;" id="fg-chem">Produits chimiques</div>'
'</div>\n'

'</div></div>\n\n'  # end dashboard

# ═══════════ 10 RULES PAGE ═══════════
'<div id="rules-page" class="view">\n'
'<div class="rules-header">\n'
'<div class="rules-header-left">'
'<div class="rules-label" id="rp-label">Terrain</div>'
'<h1 id="rp-title">10 R&#200;GLES DE PR&#201;VENTION DES ACCIDENTS</h1>'
'</div>\n'
+ LRU + '\n'
'</div>\n'
'<div style="padding:0 16px 20px;display:flex;align-items:center;gap:12px;">'
'<button class="back-btn" onclick="gotoDashboard()">&#8592;</button>'
'<span style="font-family:\'Barlow\',sans-serif;font-size:14px;color:rgba(255,255,255,.75);" id="rp-back-lbl">Retour au tableau de bord</span>'
'</div>\n'
'<div class="rules-grid">\n'

# 10 rule cards
rules = [
  ("&#128274;","LOTO — Consignation / D&#233;consignation","Toujours tester &amp; v&#233;rifier.","V&#233;rifiez l\'absence d\'&#233;nergie r&#233;siduelle avant tout travail. Verrouillez et balisez correctement les syst&#232;mes avant maintenance."),
  ("&#129438;","Protection anti-chute","Toujours s\'attacher en cas de risque de chute.","Utilisez les harnais agr&#233;&#233;s et les protections anti-chute lors de travaux en hauteur."),
  ("&#128268;","Cavaliers de pontage (Jumpers)","Toujours compter les cavaliers avant et apr&#232;s utilisation.","V&#233;rifiez et g&#233;rez soigneusement les cavaliers lors des travaux &#233;lectriques sur ascenseurs."),
  ("&#9975;","&#201;quipements de Protection Individuelle (EPI)","Toujours porter les EPI adapt&#233;s.","Chaussures de s&#233;curit&#233;, gants, casque, protections auditives et oculaires obligatoires."),
  ("&#128665;","Acc&#232;s toiture cabine et fosse","Garder le contr&#244;le de l\'ascenseur en permanence.","Respecter les proc&#233;dures d\'acc&#232;s lors de l\'entr&#233;e en fosse ou en toiture de cabine."),
  ("&#9889;","Travaux &#233;lectriques sous tension","Utiliser une seule main pour les mesures.","&#201;vitez les incidents &#233;lectriques en appliquant les proc&#233;dures de diagnostic s&#233;curis&#233;."),
  ("&#9881;","&#201;nergie m&#233;canique stock&#233;e","&#201;viter les points de pincement.","Lib&#233;rez l\'&#233;nergie m&#233;canique stock&#233;e avant d\'intervenir sur les machines."),
  ("&#128295;","Levage &amp; Grutage","V&#233;rifier la stabilit&#233; &amp; la capacit&#233;.","Inspectez les &#233;quipements de levage et ne vous placez jamais sous des charges suspendues."),
  ("&#128665;","Fausses cabines &amp; plateformes","Op&#233;rer avec deux moyens de s&#233;curit&#233;.","Utilisez les protections approuv&#233;es et s&#233;curisez les plateformes avant toute op&#233;ration."),
  ("&#9888;","Balisage","S&#233;curiser le chantier avec des barricades.","Utilisez barri&#232;res et panneaux de signalisation pour isoler les zones de travail dangereuses."),
]

for i, (icon, title, highlight, desc) in enumerate(rules, 1):
    HTML_PART = (
      '<div class="rule-card">'
      '<div class="rule-num">R&#232;gle ' + str(i) + '</div>'
      '<div class="rule-icon">' + icon + '</div>'
      '<div class="rule-title">' + title + '</div>'
      '<div class="rule-highlight">' + highlight + '</div>'
      '<div class="rule-desc">' + desc + '</div>'
      '</div>\n'
    )
    globals()['HTML'] = globals().get('HTML', '') 
    # We'll build incrementally
    pass

# Build rules HTML inline
rules_html = ''
for i, (icon, title, highlight, desc) in enumerate(rules, 1):
    rules_html += (
      '<div class="rule-card">'
      '<div class="rule-num">R&#232;gle ' + str(i) + '</div>'
      '<div class="rule-icon">' + icon + '</div>'
      '<div class="rule-title">' + title + '</div>'
      '<div class="rule-highlight">' + highlight + '</div>'
      '<div class="rule-desc">' + desc + '</div>'
      '</div>\n'
    )

RULES_SECTION = rules_html
RULES_SECTION += ('</div>\n'  # end rules-grid
'<div class="rules-quote">'
'<p>"AUCUN TRAVAIL N\'EST SI IMPORTANT OU URGENT QU\'IL NE PEUT PAS &#202;TRE FAIT EN S&#201;CURIT&#201;."</p>'
'</div>\n'
'<div class="rules-footer">'
'<span>&#128737;</span>'
'<span>OSH &#8212; PARCE QUE NOUS TENONS &#192; VOUS</span>'
'</div>\n</div>\n\n')

# ═══════════ CAMPAIGNS PAGE ═══════════
CAMPS_SECTION = (
'<div id="campaigns-page" class="view">\n'
'<div style="background:#f1f4f7;min-height:100vh;">\n'
'<div style="padding:20px 20px 0;display:flex;align-items:center;gap:14px;margin-bottom:24px;">'
'<button class="back-btn" onclick="gotoDashboard()">&#8592;</button>'
'<div><div style="font-family:\'Barlow Condensed\',sans-serif;font-size:24px;font-weight:800;color:#1a0a2e;" id="cp-title">Campagnes S&#233;curit&#233;</div>'
'<div style="font-size:13px;color:#9ca3af;" id="cp-sub">Nos initiatives pour vous ramener &#224; la maison en s&#233;curit&#233;.</div></div>'
'</div>\n'
'<div id="camp1-card" class="camp-card" onclick="void(0)">'
'<div class="camp-card-banner" style="background:linear-gradient(90deg,#6b21a8,#9333ea);"></div>'
'<div class="camp-card-body">'
'<div class="camp-card-icon">&#9889;</div>'
'<div class="camp-card-name" id="cp-c1-name">Campagne 1</div>'
'<div class="camp-card-desc" id="cp-c1-desc">Cliquez pour en savoir plus sur cette campagne de s&#233;curit&#233;.</div>'
'<div class="camp-card-arrow"><span class="camp-card-cta" id="cp-learn">En savoir plus</span><span style="color:#6a35b5;font-size:18px;">&#8594;</span></div>'
'</div></div>\n'
'<div id="camp2-card" class="camp-card" onclick="void(0)">'
'<div class="camp-card-banner" style="background:linear-gradient(90deg,#ea580c,#f97316);"></div>'
'<div class="camp-card-body">'
'<div class="camp-card-icon">&#127968;</div>'
'<div class="camp-card-name" id="cp-c2-name">Campagne 2</div>'
'<div class="camp-card-desc" id="cp-c2-desc">Cliquez pour en savoir plus sur cette campagne de s&#233;curit&#233;.</div>'
'<div class="camp-card-arrow"><span class="camp-card-cta" id="cp-learn2">En savoir plus</span><span style="color:#ea580c;font-size:18px;">&#8594;</span></div>'
'</div></div>\n'
'</div></div>\n\n'
)

# ═══════════ REPORT PAGE ═══════════
REPORT_SECTION = (
'<div id="report-page" class="view">\n'
'<div style="background:#f2f4f7;min-height:100vh;">\n'
'<div style="padding:20px 20px 0;display:flex;align-items:flex-start;gap:14px;">'
'<button class="back-btn" onclick="gotoDashboard()" style="margin-top:4px;">&#8592;</button>'
'<div>'
'<div class="report-title" id="rpt-title">Signaler</div>'
'<div class="report-sub" id="rpt-sub">Am&#233;liorez la s&#233;curit&#233; en signalant les &#233;v&#233;nements en temps r&#233;el.</div>'
'</div></div>\n'
'<div class="report-card">\n'
'<div class="alert-box ok" id="report-ok" style="display:none;">&#10003; Rapport soumis avec succ&#232;s&#160;!</div>\n'
'<div class="report-field">'
'<label class="report-label" id="rpt-type-lbl">Type de signalement</label>'
'<div class="report-icon-wrap">'
'<span class="field-icon">&#128203;</span>'
'<select class="report-input report-select" id="rpt-type" style="width:100%;">'
'<option value="" id="rpt-type-ph">S&#233;lectionnez le type</option>'
'<option value="unsafe_condition" id="rpt-o1">Condition non s&#233;curis&#233;e</option>'
'<option value="near_miss" id="rpt-o2">Presque-accident (Near Miss)</option>'
'<option value="incident" id="rpt-o3">Incident</option>'
'<option value="injury" id="rpt-o4">Blessure</option>'
'<option value="equipment_damage" id="rpt-o5">D&#233;g&#226;t mat&#233;riel</option>'
'<option value="environmental" id="rpt-o6">Risque environnemental</option>'
'</select>'
'</div></div>\n'
'<div class="report-field">'
'<label class="report-label" id="rpt-loc-lbl">Lieu</label>'
'<div class="report-icon-wrap">'
'<input class="report-input" type="text" id="rpt-location" placeholder="Entrez le lieu" />'
'<span class="field-icon" style="right:14px;left:auto;">&#128205;</span>'
'</div></div>\n'
'<div class="report-field">'
'<label class="report-label" id="rpt-dt-lbl">Date &amp; Heure</label>'
'<div class="report-icon-wrap">'
'<span class="field-icon">&#128197;</span>'
'<input class="report-input" type="datetime-local" id="rpt-datetime" />'
'</div></div>\n'
'<div class="report-field">'
'<label class="report-label" id="rpt-desc-lbl">Description</label>'
'<textarea class="report-input report-textarea" id="rpt-desc" placeholder="D&#233;crivez ce qui s\'est pass&#233;..."></textarea>'
'</div>\n'
'<div class="report-field">'
'<label class="report-label" id="rpt-act-lbl">Actions pr&#233;ventives prises</label>'
'<textarea class="report-input report-textarea" id="rpt-actions" placeholder="D&#233;crivez les mesures correctives prises..."></textarea>'
'</div>\n'
'<div class="report-field">'
'<label class="report-label" id="rpt-photo-lbl">Photo (facultatif)</label>'
'<div class="report-upload" onclick="document.getElementById(\'rpt-file\').click()">'
'<div class="upload-icon">&#9729;</div>'
'<p id="rpt-upload-txt">Appuyez pour t&#233;l&#233;charger une photo</p>'
'<input type="file" id="rpt-file" accept="image/*" style="display:none" onchange="previewPhoto(this)" />'
'</div>'
'<div id="photo-preview" style="margin-top:10px;display:none;">'
'<img id="photo-img" style="width:100%;border-radius:10px;max-height:200px;object-fit:cover;" />'
'</div>'
'</div>\n'
'<div class="alert-box err" id="report-err"></div>\n'
'<button class="report-submit" id="rpt-btn" onclick="submitReport()">Soumettre le rapport</button>\n'
'</div></div></div>\n\n'
)

# ═══════════ ADMIN LOGIN ═══════════
ADMIN_LOGIN = (
'<div id="admin-login-page" class="view">\n'
'<div style="min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#1e1b2e 0%,#3b0a8a 60%,#f97316 100%);padding:24px;">\n'
'<div style="background:white;border-radius:20px;padding:36px 28px;width:100%;max-width:380px;box-shadow:0 20px 60px rgba(0,0,0,.3);">'
'<div style="text-align:center;font-size:36px;margin-bottom:12px;">&#128274;</div>'
'<div style="font-family:\'Nunito\',sans-serif;font-size:22px;font-weight:900;color:#1e1b2e;text-align:center;margin-bottom:4px;" id="al-title">Panneau Admin</div>'
'<div style="font-size:13px;color:#9ca3af;text-align:center;margin-bottom:24px;">Safety First &#8212; TK Home Solutions</div>'
'<div class="alert-box err" id="admin-login-err"></div>\n'
'<div class="form-group"><label id="al-ul">Nom d\'utilisateur</label><input type="text" id="admin-user-input" placeholder="admin" /></div>\n'
'<div class="form-group"><label id="al-pl">Mot de passe</label><input type="password" id="admin-pass-input" placeholder="&#x2022;&#x2022;&#x2022;&#x2022;&#x2022;&#x2022;&#x2022;&#x2022;" onkeydown="if(event.key===\'Enter\')doAdminLogin()" /></div>\n'
'<button id="admin-login-btn" onclick="doAdminLogin()" class="form-submit" id="al-btn">Connexion Admin</button>\n'
'<button onclick="gotoDashboard()" style="width:100%;background:none;border:none;color:#9ca3af;font-size:13px;margin-top:14px;cursor:pointer;font-family:\'DM Sans\',sans-serif;" id="al-back">&#8592; Retour au tableau de bord</button>\n'
'</div></div></div>\n\n'
)

# ═══════════ ADMIN PANEL ═══════════
ADMIN_PANEL = (
'<div id="admin-panel-page" class="view" style="background:#f1f4f7;min-height:100vh;">\n'
'<div style="background:linear-gradient(135deg,#1e1b2e 0%,#3b0a8a 100%);padding:24px;display:flex;align-items:center;gap:16px;">'
'<button onclick="gotoDashboard()" style="background:rgba(255,255,255,.15);border:none;color:white;border-radius:10px;padding:8px 14px;cursor:pointer;font-size:13px;font-weight:700;font-family:\'Nunito\',sans-serif;" id="ap-back">&#8592; Tableau de bord</button>'
'<div style="font-family:\'Nunito\',sans-serif;font-weight:900;font-size:22px;color:white;" id="ap-title">&#9881; Administration</div>'
'</div>\n'
'<div style="padding:20px 16px 60px;max-width:700px;margin:0 auto;">\n'

# Stats
'<div class="adm-section"><h3 id="as-stats">&#128200; Statistiques du tableau de bord</h3>'
'<label class="adm-label" id="as-days-l">Jours sans accident</label><input type="number" id="a-days" class="adm-inp" placeholder="ex. 1037" />'
'<label class="adm-label" id="as-unsafe-l">Conditions non s&#233;curis&#233;es</label><input type="number" id="a-unsafe" class="adm-inp" placeholder="ex. 127" />'
'<label class="adm-label" id="as-sif-l">SIF</label><input type="number" id="a-sif" class="adm-inp" placeholder="ex. 1" />'
'<label class="adm-label" id="as-quiz-l">Score quiz</label><input type="number" id="a-quiz" class="adm-inp" placeholder="ex. 15" />'
'</div>\n'

# Safety Moment (BILINGUAL)
'<div class="adm-section"><h3 id="as-moment">&#128172; Moment S&#233;curit&#233;</h3>'
'<div style="background:#f8f6fc;border-radius:10px;padding:14px 16px;margin-bottom:16px;font-size:12px;color:#6b7280;line-height:1.5;">'
'&#128161; Ce contenu appara&#238;t dans le tableau de bord des employ&#233;s. Remplissez les deux langues.'
'</div>'
'<div class="adm-row">'
'<div><label class="adm-label" id="as-mt-fr-l">Titre (Fran&#231;ais)</label><input type="text" id="a-moment-title-fr" class="adm-inp" placeholder="Moment S&#233;curit&#233;" /></div>'
'<div><label class="adm-label" id="as-mt-en-l">Titre (English)</label><input type="text" id="a-moment-title-en" class="adm-inp" placeholder="Safety Moment" /></div>'
'</div>'
'<label class="adm-label" id="as-mt-txt-fr-l">Message (Fran&#231;ais)</label><textarea id="a-moment-fr" class="adm-inp" style="min-height:90px;resize:vertical;" placeholder="Le message de s&#233;curit&#233; de la semaine..."></textarea>'
'<label class="adm-label" id="as-mt-txt-en-l">Message (English)</label><textarea id="a-moment-en" class="adm-inp" style="min-height:90px;resize:vertical;" placeholder="Weekly safety moment message..."></textarea>'
'<div class="adm-row">'
'<div><label class="adm-label" id="as-mt-btn-fr-l">Texte bouton (FR)</label><input type="text" id="a-moment-btn-fr" class="adm-inp" placeholder="Lire plus" /></div>'
'<div><label class="adm-label" id="as-mt-btn-en-l">Texte bouton (EN)</label><input type="text" id="a-moment-btn-en" class="adm-inp" placeholder="Read More" /></div>'
'</div></div>\n'

# Campaigns (BILINGUAL)
'<div class="adm-section"><h3 id="as-camps">&#128226; Campagnes S&#233;curit&#233;</h3>'
'<div style="background:#f8f6fc;border-radius:10px;padding:14px 16px;margin-bottom:16px;font-size:12px;color:#6b7280;line-height:1.5;">'
'&#128161; Configurez les deux campagnes affich&#233;es dans le tableau de bord (ex. Stop The Shock, We Get Home).'
'</div>'

# Campaign 1
'<div style="border:1.5px solid #e5e7eb;border-radius:12px;padding:16px;margin-bottom:16px;">'
'<div style="font-family:\'Nunito\',sans-serif;font-weight:800;font-size:13px;color:#6a35b5;margin-bottom:12px;" id="as-c1">&#128308; Campagne 1</div>'
'<div class="adm-row">'
'<div><label class="adm-label" id="as-c1-fr-l">Nom (FR)</label><input type="text" id="a-camp1-fr" class="adm-inp" placeholder="Stop The Shock" /></div>'
'<div><label class="adm-label" id="as-c1-en-l">Name (EN)</label><input type="text" id="a-camp1-en" class="adm-inp" placeholder="Stop The Shock" /></div>'
'</div>'
'<label class="adm-label" id="as-c1-url-l">Lien (URL, facultatif)</label><input type="url" id="a-camp1-url" class="adm-inp" placeholder="https://..." />'
'</div>'

# Campaign 2
'<div style="border:1.5px solid #e5e7eb;border-radius:12px;padding:16px;">'
'<div style="font-family:\'Nunito\',sans-serif;font-weight:800;font-size:13px;color:#ea580c;margin-bottom:12px;" id="as-c2">&#128308; Campagne 2</div>'
'<div class="adm-row">'
'<div><label class="adm-label" id="as-c2-fr-l">Nom (FR)</label><input type="text" id="a-camp2-fr" class="adm-inp" placeholder="We Get Home" /></div>'
'<div><label class="adm-label" id="as-c2-en-l">Name (EN)</label><input type="text" id="a-camp2-en" class="adm-inp" placeholder="We Get Home" /></div>'
'</div>'
'<label class="adm-label" id="as-c2-url-l">Lien (URL, facultatif)</label><input type="url" id="a-camp2-url" class="adm-inp" placeholder="https://..." />'
'</div></div>\n'

# Users & Reports
'<div class="adm-section"><h3 id="as-users">&#128101; Comptes employ&#233;s</h3>'
'<div id="users-list" style="font-size:13px;color:#6b7280;">Chargement...</div>'
'</div>\n'

'<div class="adm-section"><h3 id="as-reports">&#128680; Rapports d\'incidents</h3>'
'<div id="reports-list" style="font-size:13px;color:#6b7280;">Chargement...</div>'
'</div>\n'

'<button id="admin-save-btn" onclick="saveAdminData()" style="width:100%;background:linear-gradient(135deg,#6b21a8,#f97316);border:none;color:white;border-radius:12px;padding:16px;font-family:\'Nunito\',sans-serif;font-size:16px;font-weight:900;cursor:pointer;" id="as-save-btn">&#128190; Sauvegarder &amp; notifier les utilisateurs</button>\n'
'<div class="alert-box ok" id="admin-save-ok" style="margin-top:12px;display:none;">&#10003; Donn&#233;es sauvegard&#233;es avec succ&#232;s&#160;!</div>\n'
'</div></div>\n\n'
)

# Assemble full HTML
FULL = (HTML + RULES_SECTION + CAMPS_SECTION + REPORT_SECTION +
        ADMIN_LOGIN + ADMIN_PANEL +
        '<script src="app.js"></script>\n</body>\n</html>')

with open('/home/claude/safety-first/public/index.html','w',encoding='utf-8') as f:
    f.write(FULL)

print("index.html written:", len(FULL), "bytes")
