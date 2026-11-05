A='fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
def s(w,sw,body,vb="0 0 24 24"): return f'<svg width="{w}" height="{w}" viewBox="{vb}" stroke-width="{sw}" {A}>{body}</svg>'
STAR='<path d="M11.52 2.3a.53.53 0 0 1 .95 0l2.31 4.68a2.12 2.12 0 0 0 1.6 1.16l5.16.76a.53.53 0 0 1 .3.9l-3.74 3.64a2.12 2.12 0 0 0-.61 1.88l.88 5.14a.53.53 0 0 1-.77.56l-4.62-2.43a2.12 2.12 0 0 0-1.97 0L6.4 21.01a.53.53 0 0 1-.77-.56l.88-5.14a2.12 2.12 0 0 0-.61-1.88L2.16 9.8a.53.53 0 0 1 .3-.91l5.16-.75a2.12 2.12 0 0 0 1.6-1.16z" fill="currentColor"></path>'
CAL='<rect width="18" height="18" x="3" y="4" rx="2"></rect><path d="M16 2v4M8 2v4M3 10h18"></path>'
PIN='<path d="M12 17v5"></path><path d="M9 10.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24V16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V7a1 1 0 0 1 1-1 2 2 0 0 0 0-4H8a2 2 0 0 0 0 4 1 1 0 0 1 1 1z"></path>'
BOX='<rect width="20" height="5" x="2" y="3" rx="1"></rect><path d="M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8"></path><path d="M10 12h4"></path>'
TAG='<path d="M12.59 2.59A2 2 0 0 0 11.17 2H4a2 2 0 0 0-2 2v7.17a2 2 0 0 0 .59 1.42l8.7 8.7a2.43 2.43 0 0 0 3.42 0l6.58-6.58a2.43 2.43 0 0 0 0-3.42z"></path><circle cx="7.5" cy="7.5" r="1.2" fill="currentColor"></circle>'
GIFT='<rect x="3" y="8" width="18" height="4" rx="1"></rect><path d="M12 8v13"></path><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"></path><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"></path>'
X='<path d="M18 6 6 18M6 6l12 12"></path>'
CHK='<path d="M20 6 9 17l-5-5"></path>'
SPARK='<path d="M12 2.5l1.9 6.6 6.6 1.9-6.6 1.9-1.9 6.6-1.9-6.6-6.6-1.9 6.6-1.9z" fill="currentColor" stroke="none"></path>'
YARN='<circle cx="10" cy="14" r="7"></circle><path d="M4.6 10.4c2.9 1.3 6.9 1.2 10.9-1.2"></path><path d="M3.3 14.8c3.4 1.4 8.3 1 12.4-2.4"></path><path d="M6.3 19.3c3-.6 6.5-2.6 9-6"></path><path d="M15.2 8.8 20.6 3.4"></path><path d="M20.6 3.4a1.3 1.3 0 0 1-.1 2.1"></path>'
TREE='<path d="m17 14 3 3.3a1 1 0 0 1-.7 1.7H4.7a1 1 0 0 1-.7-1.7L7 14h-.3a1 1 0 0 1-.7-1.7L9 9h-.2A1 1 0 0 1 8 7.3L12 3l4 4.3a1 1 0 0 1-.8 1.7H15l3 3.3a1 1 0 0 1-.7 1.7H17Z"></path><path d="M12 22v-3"></path>'
GRID='<rect width="7" height="7" x="3" y="3" rx="1.5"></rect><rect width="7" height="7" x="14" y="3" rx="1.5"></rect><rect width="7" height="7" x="14" y="14" rx="1.5"></rect><rect width="7" height="7" x="3" y="14" rx="1.5"></rect>'
COMP='<circle cx="12" cy="12" r="10"></circle><path d="m16.24 7.76-1.8 5.41a2 2 0 0 1-1.27 1.27L7.76 16.24l1.8-5.41a2 2 0 0 1 1.27-1.27z"></path>'
VID='<path d="m16 13 5.22 3.48a.5.5 0 0 0 .78-.42V7.87a.5.5 0 0 0-.75-.43L16 10.5"></path><rect x="2" y="6" width="14" height="12" rx="2"></rect>'
CLK='<circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path>'
SHIELD='<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path><path d="m9 12 2 2 4-4"></path>'
BOLT='<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"></path>'
PHONE='<rect width="14" height="20" x="5" y="2" rx="2"></rect><path d="M12 18h.01"></path>'
SPK='<path d="M11 4.7a.7.7 0 0 0-1.2-.5L6.41 7.59A1.4 1.4 0 0 1 5.42 8H3a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2.42a1.4 1.4 0 0 1 .99.41l3.39 3.39a.7.7 0 0 0 1.2-.5z"></path>'
S={
0:'<svg class="am-medio-nieve" viewBox="0 0 320 24" preserveAspectRatio="none" aria-hidden="true"><path d="M0 16c4-6 12-8 19-5 3-7 14-9 21-3 5-5 14-6 20 0 6-8 19-8 25 0 4-3 11-3 15 1 5-7 16-8 23-2 4-4 11-4 16 0 6-6 17-7 24 0 5-5 14-5 19 1 4-6 13-7 19-2 6-5 15-4 20 2 5-4 12-4 17 1 4-6 13-7 19-1 5-4 12-4 16 1 4-5 11-5 15 0 5-4 12-3 16 3v6c-3 3-7 3-9 0-2 4-7 4-9 0-3 3-8 2-9-2-4 3-9 2-11-2-3 2-7 1-8-2-4 3-10 2-12-2-4 2-8 1-10-2-3 3-9 2-10-2-4 3-9 3-11-1-4 2-9 1-10-3-4 3-10 3-12-1-3 2-7 2-9-1-4 3-10 2-11-2-4 2-9 1-11-3-3 3-8 3-10-1-4 2-9 2-11-2-3 3-8 2-9-2-4 2-8 1-10-3-3 3-8 3-10-1-2 3-7 3-9 0Z" fill="#ffffff"></path></svg>',
1:s(14,2.2,'<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0l1.58 6.14a2 2 0 0 0 1.44 1.44l6.14 1.58a.5.5 0 0 1 0 .96l-6.14 1.58a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0z"></path><path d="M20 3v4M22 5h-4"></path>'),
2:s(15,2,STAR),
3:s(16,2,'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path><path d="M14 2v4a2 2 0 0 0 2 2h4"></path><path d="M10 9H8M16 13H8M16 17H8"></path>'),
4:'<svg class="am-nevado" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true"><path d="M0 52C90 34 170 30 260 42s170 30 270 22 190-40 300-38 190 34 300 36 200-26 310-28V90H0Z" fill="#ffffff" fill-opacity=".55"></path><path d="M0 64c110-18 210-20 320-8s200 26 320 18 210-34 330-32 200 26 280 28 150-10 190-14V90H0Z" fill="#fbf7f0"></path></svg>',
5:s(22,1.75,CAL),6:s(22,1.75,PIN),7:s(22,1.75,BOX),8:s(22,1.75,TAG),9:s(22,1.75,GIFT),
10:s(11,2.2,X),11:s(15,2,X),12:s(11,2.2,CHK),13:s(16,2,'<path d="m9 18 6-6-6-6"></path>'),14:s(15,2,CHK),15:s(13,2.2,SPARK),
16:s(18,2,YARN),17:s(18,2,GIFT),18:s(18,2,TAG),19:s(12,2.2,CHK),
20:s(20,1.75,'<path d="m15 18-6-6 6-6"></path>'),21:s(20,1.75,'<path d="m9 18 6-6-6-6"></path>'),
22:s(22,1.75,TREE),23:s(22,1.75,GRID),24:s(22,1.75,COMP),25:s(22,1.75,VID),26:s(14,2.2,GIFT),27:s(16,2,CHK),28:s(16,2,X),
29:s(28,1.75,'<path d="M12 5v14M19 12l-7 7-7-7"></path>'),30:s(15,2,CLK),31:s(16,2,CLK),32:s(11,2.2,STAR),33:s(13,2.2,CHK),
34:s(14,2.2,TREE),35:s(14,2.2,GRID),36:s(14,2.2,COMP),37:s(14,2.2,VID),38:s(14,2.2,BOX),39:s(14,2.2,PHONE),
40:s(14,2.2,'<path d="M6 16c5 0 7-8 12-8a4 4 0 0 1 0 8c-5 0-7-8-12-8a4 4 0 1 0 0 8"></path>'),
41:s(16,2,'<path d="m5 8 6 6"></path><path d="m4 14 6-6 2-3"></path><path d="M2 5h12"></path><path d="M7 2h1"></path><path d="m22 22-5-10-5 10"></path><path d="M14 18h6"></path>'),
42:s(16,2,'<path d="M12 22a1 1 0 0 1 0-20 10 9 0 0 1 10 9 5 5 0 0 1-5 5h-2.25a1.75 1.75 0 0 0-1.4 2.8l.3.4a1.75 1.75 0 0 1-1.4 2.8z"></path><circle cx="13.5" cy="6.5" r=".6" fill="currentColor"></circle><circle cx="17.5" cy="10.5" r=".6" fill="currentColor"></circle><circle cx="6.5" cy="12.5" r=".6" fill="currentColor"></circle><circle cx="8.5" cy="7.5" r=".6" fill="currentColor"></circle>'),
43:s(16,2,'<rect width="16" height="20" x="4" y="2" rx="2"></rect><path d="M8 6h8M16 14v4M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"></path>'),
44:s(16,2,'<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"></path><circle cx="12" cy="13" r="3"></circle>'),
45:s(14,2.2,BOLT),46:s(18,2,SHIELD),47:s(12,2.2,SPARK),48:s(14,2.2,'<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"></path>'),
49:s(22,1.75,'<rect width="18" height="18" x="3" y="3" rx="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.09-3.09a2 2 0 0 0-2.82 0L6 21"></path>'),
50:s(17,2,STAR),51:s(40,1.75,SHIELD),52:s(16,2,'<path d="M12 5v14M5 12h14"></path>'),
53:s(14,2.2,'<rect width="18" height="11" x="3" y="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>'),
54:s(14,2.2,STAR),55:s(14,2.2,SPK+'<path d="M16 9a5 5 0 0 1 0 6"></path><path d="M19.36 18.36a9 9 0 0 0 0-12.72"></path>'),
56:s(14,2.2,SPK+'<path d="m22 9-6 6M16 9l6 6"></path>'),57:s(12,2.2,CLK),58:s(22,1.75,YARN),
}
