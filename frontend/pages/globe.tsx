import React from 'react'
import { Canvas } from '@react-three/fiber'

export default function GlobePage() {
  return (
    <main style={{height: '100vh', margin: 0}}>
      <Canvas camera={{ position: [0, 0, 3] }}>
        <ambientLight />
        <pointLight position={[10, 10, 10]} />
        <mesh>
          <sphereGeometry args={[1, 64, 64]} />
          <meshStandardMaterial color={'#88a'} />
        </mesh>
      </Canvas>
      <div style={{position: 'absolute', top: 10, left: 10, color: '#fff'}}>
        <strong>Globe placeholder</strong>
        <div>Replace material with Earth texture and add data overlays.</div>
      </div>
    </main>
  )
}
