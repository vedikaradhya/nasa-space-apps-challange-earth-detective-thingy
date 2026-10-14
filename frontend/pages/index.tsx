import Link from 'next/link'

export default function Home() {
  return (
    <main style={{padding: 40, fontFamily: 'Arial, sans-serif'}}>
      <h1>Earth System Trend Detective</h1>
      <p>Productized frontend skeleton with a 3D globe placeholder.</p>
      <Link href="/globe"><a>Open 3D Globe</a></Link>
    </main>
  )
}
