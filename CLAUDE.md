# Rules for generating the Landing Page

## Fonts to use
- Cooper BT Medium [./assets/Cooper_BT_Font_Family/]
- Poppins

## Colors to use
- Primary: Coral (Hex:#FC7F67), Black (Hex:#000000)
- Secondary: Teal (Hex:#309CAD)
- Tertiary Color: Dusty Rose (Hex:#C3A3A1)
- Background: Off White (Hex:#FFFFFD)
- Supporting Colors:
  - Descriptions / Paragraphs: Grey (Hex:#999999)
  - Subtext / Plaveholder text: Light Grey (Hex:#A5A9AC)

## Sections required

### Hero Section
- Starts with the (Logo)[./assets/Logo.png]
- Has the first line Hero Text: `Meet Rosy!`
- Second line Hero Text: `Your AI Parenting Co-pilot`
- The two hero text lines must be wrapped around a single `<h1>` tag for SEO purposes
- Third Line paragraph text: `AI assistant for expert based parenting guidance, milestone tracking, and more`
- Finally a `Join the waitlist` CTA
- (Reference Image)['./assets/Hero Section.png']

### How it works section
- Starts with the Header for this section in `<h2>`: `Rosy makes your parenting experience a delight`
- Then followed by 3 features:
  - Empathetic chat: Rosy's caring AI chat offers support, advice, and makes you feel truly understood.
  - Chat to track: Rosy transforms your messages into actionable insights and tracks your parenting journey.
  - Chat to shop: Rosy assists you in finding the right products to meet your family's needs with ease.
- Each feature will have their own `Watch Demo ->` CTA.
- (Reference Image)['./assets/Features.png']

### Watch how Rosy works
- Starts with the Header for this section in `<h2>`: `Watch how Rosy works`
- Followed by a paragraph text: `See the magic placeholder`
- Placeholder for a video
- (Reference Image)['./assets/Watch how Rosy works.png']

### Social Proof
- Starts with the Header for this section in `<h2>`: `Trusted by Parents`
- Followed by a paragraph text: `Parents with early-access trust Rosy to help lighten the load`
- 3 Social Proofs with dummy data for now
- (Reference Image)['./assets/Social proof.png']

### Join the waitlist
- CTA form to join the waitlist

### Socials + Sharing
- Link to socials
- CTA to share Rosy landing page [userosy.ai]

### Footer
- Simple footer just showing the rights as of the year `2025`

## Rules to abide in development
- The whole landing page must be made of just HTML and CSS
- If and only if backend is required, especially to capture Waitlist form input, then use python with postgres. I'll link Supabase to it.
- Animations are required to make the site look completely modern. I'll leave it to your descretion to decide what kind of animation.
- The entire site must be mobile responsive. This is a MUST HAVE.
- Each section should scroll to the next section smoothly.
- At any given scrolling portion, one section should be clearly seen. You can use animations to make it look as though one scroll is enough to get to the next section. This kind of animation might have to be slightly different for mobile screen.
- Ensure you use the images provided to understand the colors and font usage.
- Background color is Off White.
